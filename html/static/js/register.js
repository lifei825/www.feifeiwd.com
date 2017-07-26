    function openLogin(){
            document.getElementById("win").style.display="";
                document.getElementById("back").style.display="";
                    }
    function openRegist(){
            document.getElementById("winre").style.display="";
                document.getElementById("back").style.display="";
                    }

    function closeLogin(){
            document.getElementById("win").style.display="none";
                document.getElementById("back").style.display="none";
                    }
    function closeRegist(){
            document.getElementById("winre").style.display="none";
                document.getElementById("back").style.display="none";
                    }


function check_form(){
    if(forms.username.value==""||forms.passwd1.value==""){
    alert("用户名OR密码不能为空！");
    document.forms.username.focus();
    return false;
    }

    if(document.forms.username.value.length>30){
    alert("用户名不能超过30个字符！");
    document.forms.username.focus();
    return false;
    }

    if(forms.passwd1.value != forms.passwd2.value){
    alert("两次密码不一致！请重新输入");
    document.forms.passwd1.focus();
    return false;
    }
    
    if(forms.passwd1.value.length<6){
    alert("密码最少6位！请重新输入");
    document.forms.passwd1.focus();
    return false;
    }
    return true;
}

function check_form_login(){
    if(formslogin.username.value==""||formslogin.password.value==""){
    alert("用户名OR密码不能为空！");
    document.formslogin.username.focus();
    return false;
    }
    return true
}
