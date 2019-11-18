# Concept before starting/using Celery.
## 
 
Ref. https://www.distributedpython.com/2018/10/26/celery-execution-pool/
# Celery Execution Pools: What is it all about?
An introduction to prefork, solo, eventlet and gevent 
Have you ever asked yourself what happens when you start a Celery worker? Ok, 
it might not have been on your mind. But you might have come across things 
like execution pool, concurrency settings, prefork, gevent, eventlet and solo. 
So, what is it all about? How does it all fit together? And how is it related 
to the mechanics of a Celery worker?

## The Celery worker
When you start a Celery worker on the command line via celery --app=..., you just start 
a supervisor process. The Celery worker itself does not process any tasks. 
It spawns child processes (or threads) and deals with all the book keeping stuff. 
The child processes (or threads) execute the actual tasks. These child processes (or threads) 
are also known as the execution pool. The size of the execution pool determines the number 
of tasks your Celery worker can process . The more processes (or threads) the worker spawns, 
the more tasks it can process concurrently. If you need to process as many tasks as 
quickly as possible, you need a bigger execution pool. At least, that is the idea.
In reality, it is more complicated. The answer to the question how big your execution 
pool should be, depends whether you use processes or threads. And the answer to the question 
whether you should use processes or threads, depends what your tasks actually do.

## The –pool option
You can choose between processes or threads, using the --pool command line argument. Use 
a gevent execution pool, spawning 100 green threads (you need to pip-install gevent):

    celery worker --app=worker.app --pool=gevent --concurrency=100

Don’t worry too much about the details for now (why are threads green?). We will go into 
more details if you carry on reading. Celery supports four execution pool implementations:
    - prefork
    - solo
    - eventlet
    - gevent
The --pool command line argument is optional. If not specified, Celery defaults to the 
prefork execution pool.

## Prefork
The prefork pool implementation is based on Python’s multiprocessing  package. 
(https://docs.python.org/dev/library/multiprocessing.html#module-multiprocessing)
It allows your Celery worker to side-step Python’s Global Interpreter Lock and fully 
leverage multiple processors on a given machine. You want to use the prefork pool if your 
tasks are CPU bound. A task is CPU bound, if it spends the majority of its time 
using the CPU (crunching numbers). Your task could only go faster if your CPU were faster.
The number of available cores limits the number of concurrent processes. It only makes 
sense to run as many CPU bound tasks in parallel as there are CPUs available. Which is 
why Celery defaults to the number of CPUs available on the machine, if the –concurrency 
argument is not set. Start a worker using the prefork pool, using as many processes as 
there are CPUs available:

    celery worker --app=worker.app

## Solo
The solo pool is a bit of a special execution pool. Strictly speaking, the solo pool is neither 
threaded nor process-based. And more strictly speaking, the solo pool is not even a pool as 
it is always solo. And even more strictly speaking, the solo pool contradicts the principle 
that the worker itself does not process any tasks.
The solo pool runs inside the worker process. It runs inline which means there is no 
bookkeeping overhead. Which makes the solo worker fast. But it also blocks the worker 
while it executes tasks. Which has some implications when remote-controlling workers.

    celery worker --app=worker.app --pool=solo

The solo pool is an interesting option when running CPU intensive tasks in a microservices 
environment. In a Docker Swarm or Kubernetes context, managing the worker pool size can 
be easier than managing multiple execution pools. Instead of managing the execution pool size 
per worker(s) you manage the total number of workers.

## Eventlet and gevent
Let’s say you need to execute thousands of HTTP GET requests to fetch data from external 
REST APIs. The time it takes to complete a single GET request depends almost entirely on 
the time it takes the server to handle that request. Most of the time, your tasks wait for 
the server to send the response, not using any CPU. 

The bottleneck for this kind of task is not the CPU. The bottleneck is waiting for an Input/Output 
operation to finish. This is an Input/Output-bound task (I/O bound). The time the task 
takes to complete is determined by the time spent waiting for an input/output operation to finish.

If you run a single process execution pool, you can only handle one request at a time. It 
takes a long time to complete those thousands of GET requests. So you spawn more processes. 
But there is a tipping point where adding more processes to the execution pool has a negative 
impact on performance. The overhead of managing the process pool becomes more expensive 
than the marginal gain for an additional process.

In this scenario, spawning hundreds (or even thousands) of threads is a much more efficient 
way to increase capacity for I/O-bound tasks. Celery supports two thread-based execution 
pools: eventlet and gevent. Here, the execution pool runs in the same process as the 
Celery worker itself. To be precise, both eventlet and gevent use greenlets and not threads. 

Greenlets - also known as green threads, cooperative threads or coroutines - give you threads, 
but without using threads. Threads are managed by the operating system kernel. The operating 
system uses a general-purpose scheduler to switch between threads. This general-purpose 
scheduler is not always very efficient.

Greenlets emulate multi-threaded environments without relying on any native operating 
system capabilities. Greenlets are managed in application space and not in kernel space. T
here is no scheduler pre-emptively switching between your threads at any given moment. 
Instead your greenlets voluntarily or explicitly give up control to one another at specified 
points in your code.

This makes greenlets excel at at running a huge number of non-blocking tasks. Your application 
can schedule things much more efficiently. For a large number of tasks this can be a lot more 
scalable than letting the operating system interrupt and awaken threads arbitrarily.

For us, the benefit of using a gevent or eventlet pool is that our Celery worker can do 
more work than it could before. This means we do not need as much RAM to scale up. This 
optimises the utilisation of our workers.

Start a Celery worker using a gevent execution pool with 500 worker threads 
(you need to pip-install gevent):

    celery worker --app=worker.app --pool=gevent --concurreny=500

Start a Celery worker using a eventlet execution pool with 500 worker threads 
(you need to pip-install eventlet):

    celery worker --app=worker.app --pool=eventlet --concurreny=500

Both pool options are based on the same concept: Spawn a greenlet pool. The difference is that 
–pool=gevent uses the gevent Greenlet pool  (gevent.pool.Pool). Whereas –pool=eventlet 
uses the eventlet Greenlet pool (eventlet.GreenPool).

gevent and eventlet are both packages that you need to pip-install yourself. There are 
implementation differences between the eventlet and gevent packages. Depending on 
your circumstances, one can perform better than the other. It is worthwhile trying out both.

## The –concurrency option
To choose the best execution pool, you need to understand whether your tasks are 
CPU- or I/O-bound. CPU-bound tasks are best executed by a prefork execution pool. I/O bound 
tasks are best executed by a gevent/eventlet execution pool.

The only question remains is: how many worker processes/threads should you start? 
The --concurrency command line argument determines the number of processes/threads:

    celery worker --app=worker.app --concurrency=2

This starts a worker with a prefork execution pool which is made up of two processes. For 
prefork pools, the number of processes should not exceed the number of CPUs. 

Spawn a Greenlet based execution pool with 500 worker threads:

    celery worker --app=worker.app --pool=gevent --concurrency=500

If the --concurrency argument is not set, Celery always defaults to the number of CPUs, 
whatever the execution pool.

This makes most sense for the prefork execution pool. But you have to take it with a grain of 
salt. If there are many other processes on the machine, running your Celery worker with as 
many processes as CPUs available might not be the best idea.

Using the default concurrency setting in for a gevent/eventlet pool is almost outright stupid. 
The number of green threads it makes sense for you to run is unrelated to the number of 
CPUs you have at your disposal.

Another special case is the solo pool. Even though you can provide the --concurrency command 
line argument, it meaningless for this execution pool. 

For these reasons, it is always a good idea to set the --concurrency command line argument.

## 5 - Conclusion
Celery supports two concepts for spawning its execution pool: Prefork and Greenlets. Prefork 
is based on multiprocessing and is the best choice for tasks which make heavy use of CPU 
resources. Prefork pool sizes are roughly in line with the number of available CPUs 
on the machine.

Tasks that perform Input/Output operations should run in a greenlet-based execution pool. 
Greenlets heave like threads, but are much more lightweight and efficient. Greenlet pools 
can scale to hundreds or even thousands of tasks .

What can you do if you have a mix of CPU and I/O bound tasks? Set up two queues with one 
worker processing each queue. One queue/worker with a prefork execution pool for CPU 
heavy tasks. And another queue/worker with a gevent or eventlet execution pool 
for I/O tasks. And don’t forget to route your tasks to the correct queue.

#### Recommandation
If you have CPU bound tasks and IO bound tasks, my recommendation would be to set up 
one worker for the CPU bound tasks and one worker for the IO bound tasks. Each worker 
should has to consume a dedicated queue. On the producer side you need to ensure you 
send the CPU bound tasks and the IO bound tasks to their dedicated queues respectively, 
so they get consumed by the correct worker.

When you use a process pool, the Celery worker spawns the number of process upon startup 
and not upon receiving requests. Equally, when finishing a task, the process stays alive 
until the worker shuts down (or the process dies unexpectedly in which case Celery will 
start up a new one). In other words, each process is "pre-allocated" by default. Does that 
answer your question?

