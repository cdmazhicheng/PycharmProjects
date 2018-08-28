//百度地图展示信息模块

var map = new BMap.Map("map"); // 创建地图实例
var point = new BMap.Point(chengdupoint[0], chengdupoint[1]); // 创建点坐标
map.centerAndZoom(point, 13);   // 初始化地图，设置中心点坐标和地图级别
map.enableScrollWheelZoom(true);     //开启鼠标滚轮缩放
var mapStyle={style : "normal"}  //地图模板选择
map.setMapStyle(mapStyle);  //实现地图模板
//多地址显示坐标点
var coordinate_points = coordinatepoints
var coordinate_points_json = coordinate_points.replace(/\&quot;/g, '\"');
var coordinate_points_json_result = JSON.parse(coordinate_points_json);
//多地址显示名称
var coordinate_names = coordinatenames
var coordinate_names_json = coordinate_names.replace(/\[|\]|\&|quot;/g,'')
var coordinate_names_split = coordinate_names_json.split(",")
//多地址显示概述
var fivesite_sum_result = fivesitesumresult
var fivesite_sum_result_json = fivesite_sum_result.replace(/\[|\]|\&|quot;/g,'')
var fivesite_sum_result_split = fivesite_sum_result_json.split(",")
//概述框
var opts = {
    width : 300,
    height : 300,
    title: "信息概览"
}
messages_arr = []
var messages_obj = new Object()
//循环展示
for(var i=0;i<coordinate_points_json_result.length;i++){
    var points = new BMap.Point(coordinate_points_json_result[i][0], coordinate_points_json_result[i][1]); // 创建点
    var markers = new BMap.Marker(points);// 创建标注
    map.addOverlay(markers);    //增加点
    var label = new BMap.Label(coordinate_names_split[i], {offset:new BMap.Size(-10,-20)})// 增加标签
    //label 添加样式
    label.setStyle({
        width: "120px",
        color: '#fff',
        background: '#ff8355',
        border: '1px solid "#ff8355"',
        borderRadius: "5px",
        textAlign: "center",
        height: "26px",
        lineHeight: "26px"
    });

    markers.setLabel(label)
    //增加概述
    var four_k = i*5
    var messages = '<ul class="list-group">'+
            '<li class="list-group-item">'+'</li>'+
            '<li class="list-group-item">'+'单飞平均消费：￥'+ fivesite_sum_result_split[four_k] +'</li>'+
            '<li class="list-group-item">'+'联系电话：'+ fivesite_sum_result_split[four_k+1] +'</li>'+
            '<li class="list-group-item">'+'场地数量：'+ fivesite_sum_result_split[four_k+2] + '个'+'</li>'+
            '<li class="list-group-item">'+'营业时间：'+ fivesite_sum_result_split[four_k+3] +'</li>'+
            '<li class="list-group-item">'+'场地消费：￥'+ fivesite_sum_result_split[four_k+4] +'</li>'+
            '</ul>'
    //概述对象赋值
    messages_obj[i] = messages
    markers.setTitle(i)//设置一个定位标志，用于确认marker是哪个
    markers.addEventListener("click", function () {
        var infoWindow = new BMap.InfoWindow(messages_obj[this.getTitle()], opts)
        this.openInfoWindow(infoWindow, points)
    })
}
