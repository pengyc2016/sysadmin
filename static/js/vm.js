        function vm(){
            var sel1=document.getElementsByName('cluster')[0].value;
            var sel2=document.getElementsByName('pm')[0].value;
                    if (sel1 !="" && sel2 ==""){
                       document.getElementById("id_pm").style.display="none";
                       document.getElementById("pm_label").style.display="none";
                       document.getElementById("pm_div").style.display="none";
                       document.getElementById("id_pm").value="";
                    }
                    if (sel2 !="" && sel1 ==""){
                       document.getElementById("id_cluster").style.display="none";
                       document.getElementById("cluster_label").style.display="none";
                       document.getElementById("cluster_div").style.display="none";
                       document.getElementById("id_cluster").value="";
                    }
                    if (sel2 !="" && sel1 !=""){
                       alert("只能选物理机或集群，不能都选")
                    } 

       }
        function ipshuli(){
            var sel3=document.getElementsByName('ipcount')[0].value;
                    if (sel3 =="1"){
                       document.getElementById("vip_div").style.display="none";
                       document.getElementById("vip").value="";
                       document.getElementById("scanip_div").style.display="none";
                       document.getElementById("scanip").value="";
                    }
                    if (sel3=="2"){
                       document.getElementById("vip_div").style.display="none";
                       document.getElementById("vip").value="";
                       document.getElementById("scanip_div").style.display="none";
                       document.getElementById("scanip").value="";
                       document.getElementById("vip_div").style.display="block";
                    }
                    if (sel3 =="3"){
                       document.getElementById("vip_div").style.display="none";
                       document.getElementById("vip").value="";
                       document.getElementById("scanip_div").style.display="none";
                       document.getElementById("scanip").value="";
                       document.getElementById("vip_div").style.display="block";
                       document.getElementById("scanip_div").style.display="block";
                    } 

       }
