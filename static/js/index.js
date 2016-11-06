
var log = function(){
    console.log(arguments)
}

// 初始化百度地图
var initMap = function(){
	// 百度地图API功能
	map = new BMap.Map("allmap");    // 创建Map实例
	map.centerAndZoom(new BMap.Point(113.993, 22.551), 13);  // 初始化地图,设置中心点坐标和地图级别
	map.addControl(new BMap.MapTypeControl());   //添加地图类型控件
	map.setCurrentCity("深圳");          // 设置地图显示的城市 此项是必须设置的

    var top_left_control = new BMap.ScaleControl({
        anchor: BMAP_ANCHOR_TOP_LEFT
    });// 左上角，添加比例尺
    var top_left_navigation = new BMap.NavigationControl();  //左上角，添加默认缩放平移控件
    map.addControl(top_left_control);
    map.addControl(top_left_navigation);
    map.enableScrollWheelZoom(true);     // 开启鼠标滚轮缩放 
}

// 创建函数，在地图上添加标注
var addMarker = function(){

    // var map = new BMap.Map("container");    
    var point = new BMap.Point(113.933, 22.551);    
    var marker = new BMap.Marker(point);        // 创建标注    
    map.addOverlay(marker);                     // 将标注添加到地图中


    // 设置信息窗口内容
    sContent = "<p>职位</p>";
    infoWindow = new BMap.InfoWindow(sContent);  // 创建信息窗口对象

    marker.addEventListener("click", function() {
        this.openInfoWindow(infoWindow);  // 开启窗口信息
        //return document.getElementById("imgDemo").onload = function() {
        //    return infoWindow.redrow();
        //};
    });
}


var geoPoint = function(data){
// 创建地址解析器实例
	var myGeo = new BMap.Geocoder();
	// 将地址解析结果显示在地图上,并调整地图视野
    var addr = data['addr']
    var financeStage = data['financeStage']
    var workYear = data['workYear']
    var createTime = data['createTime']
    var positionLables = data['positionLables']
    var salary = data['salary']
    var businessZones = data['businessZones']
    var city = data['city']
    var positionName = data['positionName']
    var district = data['district']
    var companyLabelList = data['companyLabelList']
    var positionAdvantage = data['positionAdvantage']
    var jobNature = data['jobNature']
    var companySize = data['companySize']
    var industryField = data['industryField']
    var formatCreateTime = data['formatCreateTime']
    // education = data['education']
    var companyFullName = data['companyFullName']
    var companyLogo = data['companyLogo']
    var compURL = data['compURL']


	myGeo.getPoint(addr, function(point){
		if (point) {
			// map.centerAndZoom(point, 14);
            var marker = new BMap.Marker(point)
			map.addOverlay(marker);

            // 设置信息窗口内容
            var sContent = `
            <p>职位：${positionName}</p>
            <p>公司：${companyFullName}</p>
            <p>资金：${financeStage}</p>
            <p>地址：${addr}</p>
            <p>待遇：${salary}</p>
            <p>工作年限：${workYear}</p>
            <p>发布：${formatCreateTime}</p>
            <p>来源：<a href='${compURL}' target="_blank">拉勾</a></p>
            `
            
            var infoWindow = new BMap.InfoWindow(sContent);  // 创建信息窗口对象

            marker.addEventListener("click", function() {
                this.openInfoWindow(infoWindow);  // 开启窗口信息

            });
		}else{
			alert("您选择地址没有解析到结果!");
		}
	}, "深圳市");

 
}

var apiGetJob = function(){
   var response = function(data){
        log('yes you get it')
        var i, job, len, ref, results;
        if ((data.error == null) || data.error != 0) {
            return true;
        }
        ref = data["items"];
        log(ref)
        results = [];
        for (i=0, len=ref.length; i<len; i++){
            // addr = ref[i].addr
            // log(addr)
            geoPoint(ref[i])
        }
    }


     $.ajax({
        type:"get",
        url:"/api/jobs",
        // data:'mydata',    //发送到服务器的数据，可以自行构造
        dataType:"json",    //预期服务器返回的数据类型
        success:response    //callback回调函数，这里一般可要求服务器返回特定数据
    });
}

$(document).ready(function(){

    log('hello map')
    
    // 百度地图API功能
    initMap()
    // 在地图上添加标注
    // addMarker()
    // 地址解析器
    // geoPoint()

    // 在地图上添加标注
    apiGetJob();

})