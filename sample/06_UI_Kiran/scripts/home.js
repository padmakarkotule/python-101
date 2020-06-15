function makeNetworkCall() {
  $.ajax({
    type: "GET",
    url: "../json/network.json",
    dataType: "json",
    success: function (data) {
      generateNetworkList(data.result);
    },
    error: function (jqXhr, textStatus, errorMessage) {
      console.log("Error" + errorMessage);
    },
  });
}

function getAllNetworkNodes(e) {
  $.ajax({
    type: "GET",
    url: "../json/networkContent.json",
    dataType: "json",
    success: function (data) {
      $("#alertMessage").removeClass("hidden").addClass("alert-success");
      $("#alertMessage .content").html("Your request has been successful");
      generateNodeList(data.result, e);
    },
    error: function (jqXhr, textStatus, errorMessage) {
      console.log("Error" + errorMessage);
    },
  });
}

function requestNetworkNodes(requestParam) {
  $.ajax({
    type: "POST",
    url: "../json/requestNetwork.json",
    data: requestParam,
    dataType: "json",
    success: function (data) {
      $("#alertMessage").removeClass("hidden").addClass("alert-success");
      $("#alertMessage .content").html(
        data.reserved_ip_success.join() + " IP addresses has been reserved"
      );
    },
    error: function (jqXhr, textStatus, errorMessage) {
      console.log("Error" + errorMessage);
    },
  });
}
function initiateHome() {
  let selectedList = [],
    nodeListData = [];
  makeNetworkCall();
  generateNetworkList = (dataList) => {
    var dataString = "";
    for (let i = 0; i < dataList.length; i++) {
      dataString =
        dataString +
        "<div class='panel panel-default'><div class='panel-heading' role='tab' id='" +
        "heading" +
        i +
        "'><h4 class='panel-title'><a role='button' data-toggle='collapse' data-parent='#accordion' href='" +
        "#collapse" +
        i +
        "' aria-expanded='false' aria-controls='" +
        "collapse" +
        i +
        "' class='link'>" +
        "Network Name : " +
        dataList[i].network +
        "</a></h4></div><div id='" +
        "collapse" +
        i +
        "' class='panel-collapse collapse' role='tabpanel' aria-labelledby='" +
        "heading" +
        i +
        "'><div class='panel-body'></div></div></div>";
    }
    $("#networkSection #accordion").append(dataString);
  };

  generateNodeList = (data, e) => {
    let nodeList = "";
    let isDisabled;
    nodeListData = data;
    for (let i = 0; i < data.length; i++) {
      isDisabled = data[i].status == "USED" ? true : false;
      if (data[i].status == "USED") {
        nodeList =
          nodeList +
          "<input type='checkbox' id='" +
          "networkIP" +
          i +
          "' data-network-id='" +
          data[i].ip_address +
          "' class='inputBox' disabled>";
      } else {
        nodeList =
          nodeList +
          "<input type='checkbox' id='" +
          "networkIP" +
          i +
          "' data-network-id='" +
          data[i].ip_address +
          "' class='inputBox'>";
      }
    }
    nodeList =
      nodeList +
      "<section class='btn-wrapper'><button class='requestNetwork'>Request</button><button  class='releaseNetwork'>Release</button></section>";
    $(e.parentElement.parentNode.nextElementSibling.children[0]).append(
      nodeList
    );
  };

  $(document).on("click", ".link", function () {
    nodeListData = [];
    $(".panel-body").empty();
    if (!$(this).hasClass("collapsed")) {
      getAllNetworkNodes(this);
      selectedList = [];
    }
  });

  $(document).on("click", ".inputBox", function () {
    selectedList.push($(this).attr("data-network-id"));
  });

  $(document).on("click", ".requestNetwork", function () {
    const requestParam = {};
    requestParam.ip = selectedList;
    requestParam.userid = "5e5e2db6479496447c8f3a0e";
    requestNetworkNodes(JSON.stringify(requestParam));
  });

  $(document).on("click", "#alertMessage .close", function () {
    $("#alertMessage").addClass("hidden");
  });

  /*Dashboard Graphs Code Starts*/
  Highcharts.chart("container", {
    chart: {
      plotBackgroundColor: null,
      plotBorderWidth: null,
      plotShadow: false,
      type: "pie",
    },
    title: {
      text: "vCenter Cluster Data",
    },
    tooltip: {
      pointFormat: "{series.name}: <b>{point.percentage:.1f}%</b>",
    },
    accessibility: {
      point: {
        valueSuffix: "%",
      },
    },
    plotOptions: {
      pie: {
        allowPointSelect: true,
        cursor: "pointer",
        dataLabels: {
          enabled: true,
          format: "<b>{point.name}</b>: {point.percentage:.1f} %",
        },
      },
    },
    series: [
      {
        name: "Brands",
        colorByPoint: true,
        data: [
          {
            name: "Chrome",
            y: 61.41,
            sliced: true,
            selected: true,
          },
          {
            name: "Internet Explorer",
            y: 11.84,
          },
          {
            name: "Firefox",
            y: 10.85,
          },
          {
            name: "Edge",
            y: 4.67,
          },
          {
            name: "Safari",
            y: 4.18,
          },
          {
            name: "Sogou Explorer",
            y: 1.64,
          },
          {
            name: "Opera",
            y: 1.6,
          },
          {
            name: "QQ",
            y: 1.2,
          },
          {
            name: "Other",
            y: 2.61,
          },
        ],
      },
    ],
  });
  /*Dashboard Graphs Code Ends*/
}
