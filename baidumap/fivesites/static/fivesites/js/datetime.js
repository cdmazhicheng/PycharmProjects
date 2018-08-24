//显示日期和时间

function showTime(){
    nowtime=new Date();
    year=nowtime.getFullYear();
    month=nowtime.getMonth()+1;
    date=nowtime.getDate();
    document.getElementById("mytime").innerText=year+"年"+month+"月"+date+"日"+nowtime.toLocaleTimeString();
}
setInterval("showTime()",1000);