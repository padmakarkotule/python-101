pipeline {
    agent { label 'test-k8s-slave' }
    environment {
        index = "index.html"
    }
    stages {
        stage('GENERATE-REPORTING-BASE-STRUCTURE') {
            steps {
                //create index.html
                createIndTemp("${index}","${JOB_NAME}",
                    "${BUILD_NUMBER}","${BUILD_URL}","${JOB_URL}")
            }
        } //End of GENERATE-REPORTING-BASE-STRUCTURE
        stage('BUILD ENV SETUP') {
            steps {
                dir('demo') {
                    checkout([
                        $class: 'GitSCM',
                        branches: [[name: "*/master"]],
                        poll: false,
                        doGenerateSubmoduleConfigurations: false,
                        extensions: [],
                        submoduleCfg: [],
                        userRemoteConfigs: [[
                            credentialsId: 'bitbucket_user',
                            url: "https://bitbucket.example.com/demo.git"
                        ]]
                    ])
                }
            }
            post {
                always {
                    stage_status_msg("${STAGE_NAME}","${currentBuild.currentResult}")
                }
            }
        } //End of BUILD-ENV-SETUP
        stage ('BUILD JOB') {
            steps {
                script {
                    sh "
                        #build docker image
                        make docker
                    "
                }
            }
            post {
                always {
                    script {
                        stage_status_msg("${STAGE_NAME}","${currentBuild.currentResult}")
                    }
                }
            }
        } // End of ARTIFACTORY CONFIGURATION
        stage('CREATE CONTAINER') {
            steps {
                script {
                    try {
                        sh """
                         docker run -d -it -p 80:80 -p 443:443 --name container_name <docker image>
                        """
                    }
                    catch (exc) {
                        echo "Failed to run docker container"
                        throw exc
                    }
                }
            }
            post {
                always {
                    script {
                        stage_status_msg("${STAGE_NAME}","${currentBuild.currentResult}")
                    }
                }
            }
        } // End of COPY JVM TO LOCAL REPO
        stage('TEST DOCKER CONTAINER') {
            steps {
                script {
                    try {
                        withEnv(['ANSIBLE_CONFIG=ansible_json.cfg','JUNIT_OUTPUT_DIR=./'])
                        {
                            ansiblePlaybook([
                                playbook: "playbooks/test.yaml",
                                extraVars: [
                                    container_name: "demo",
                                    http_port : "80",
                                    https_port: "443",
                                ]
                            ])
                        }
                    }
                    catch (exc) {
                        echo "Failed to test container"
                    }
                }
            }
            post {
                always {
                    script {
                        stage_status_msg("${STAGE_NAME}","${currentBuild.currentResult}")
                    }
                }
            }
        } // End of BUILD UDX LIB
        stage('PUBLISH ARTIFACTS') {
            steps {
                script {
                    // Steps to publish artifacts to gcp/s3
                }
            }
            post {
                always {
                    script {
                        stage_status_msg("${STAGE_NAME}","${currentBuild.currentResult}")
                    }
                }
            }
        } // End of PUBLISH ARTIFACTS
    } // End of stages
    post {
        always {
            script {
                emailext attachLog: true, \
                    body: '''${FILE, path="index.html"}''', \
                    to: 'demo@example.com', \
                    recipientProviders: [[$class: 'RequesterRecipientProvider'], \
                                        [$class: 'DevelopersRecipientProvider'], \
                                        [$class: 'UpstreamComitterRecipientProvider']], \
                    subject: '$PROJECT_NAME - Build # $BUILD_NUMBER - $BUILD_STATUS'
                cleanWs()
            }
        }
    }
}


def createIndTemp(index,JOB_NAME,BUILD_NUMBER,BUILD_URL,JOB_URL) {
  sh '''
    #!/bin/bash
    cat > index.html <<-EOF
    <html><head><title>$JOB_NAME Report</title><style>
    #TestCategory {
        font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
        width: 100%;
        border-collapse: collapse;
    }
    #TestCategory td, #TestCategory th {
        font-size: 1em;
        border: 1px solid #000000;
        padding: 3px 7px 2px 7px;
    }
    #TestCategory th {
        font-size: 1.1em;
        text-align: left;
        padding-top: 5px;
        padding-bottom: 4px;
        background-color: #1E90FF;
    }
    </style></head>
    <body>
    <font face="Trebuchet MS, Arial, Helvetica, sans-serif">
    <p><b>Build Number: </b>${BUILD_NUMBER}</p>
    <p><b>Logs: </b>
    <a href="${BUILD_URL}/Logs">All Logs</a></p>
    <p><b>Workflow View: </b>
    <a href="${JOB_URL}/workflow-stage/">Workflow</a></p>
    <table border="1" id="TestCategory">
    <tr><th>Step</th><th>Status</th></tr>
EOF
  '''
}



def stage_status_msg(stage_name, result) {
    script {
        echo "${stage_name} => ${result}"
        sh "echo '<tr><td>${stage_name}</td><td>' >> ${index}"
        if ( "${result}" == "SUCCESS" ) {
            sh "echo '<font color='green'>${result}</font></td></tr>' >> ${index}"
        } else {
            sh "echo '<font color='red'>${result}</font></td></tr>' >> ${index}"
        }
    }
}