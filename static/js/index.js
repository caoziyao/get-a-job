
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
    log('在地图上添加标注')

    // var map = new BMap.Map("container");    
    var point = new BMap.Point(113.933, 22.551);    
    var marker = new BMap.Marker(point);        // 创建标注    
    map.addOverlay(marker);                     // 将标注添加到地图中


    // 设置信息窗口内容
    sContent = "<p>职位</p>";
    infoWindow = new BMap.InfoWindow(sContent);  // 创建信息窗口对象

    return marker.addEventListener("click", function() {
            this.openInfoWindow(infoWindow);  // 开启窗口信息
            //return document.getElementById("imgDemo").onload = function() {
            //    return infoWindow.redrow();
            //};
        });
}

$(document).ready(function(){

    log('hello map')
    
    // 百度地图API功能
    initMap()
    // 在地图上添加标注
    addMarker()

})