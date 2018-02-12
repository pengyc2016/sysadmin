        function listchange(){
            var sel=document.getElementsByName('role')[0].value;
                    if (sel=="物理集群宿主机"){
                       document.getElementById("id_project").disabled=true;
                       document.getElementById("id_vlangroup").disabled=true;
                       document.getElementById("id_storagegroup").disabled=true;
                       document.getElementById("id_cluster").disabled=true;
                       document.getElementById("id_soft").disabled=true;
                       document.getElementById("id_domain").disabled=true;
                       document.getElementById("id_cluster").disabled = false;
                    }
                    if (sel=="物理单机宿主机"){
                       document.getElementById("id_project").disabled=true;
                       document.getElementById("id_vlangroup").disabled=true;
                       document.getElementById("id_storagegroup").disabled=true;
                       document.getElementById("id_cluster").disabled=true;
                       document.getElementById("id_soft").disabled=true;
                       document.getElementById("id_domain").disabled=true;
                       document.getElementById("id_vlangroup").disabled = false;
                       document.getElementById("id_storagegroup").disabled = false;
                    }
                    if (sel=="物理单机"){
                       document.getElementById("id_project").disabled=true;
                       document.getElementById("id_vlangroup").disabled=true;
                       document.getElementById("id_storagegroup").disabled=true;
                       document.getElementById("id_cluster").disabled=true;
                       document.getElementById("id_soft").disabled=true;
                       document.getElementById("id_domain").disabled=true;
                       document.getElementById("id_vlangroup").disabled = false;
                       document.getElementById("id_storagegroup").disabled = false;
                       document.getElementById("id_project").disabled = false;
                       document.getElementById("id_soft").disabled = false;
                       document.getElementById("id_domain").disabled = false;
                    }
 

       }
