function APKmodalClose() {
    document.body.style.overflowY = 'auto';
    document.getElementById("warning_apk").style.display = 'none';
}

function APKmodalOpen() {

    if(window.apkpopup_mode != undefined) {

        if ((window.apkpopup_mode == 1 && getCookie('APK_MODAL_SHOWED') == undefined) || (window.apkpopup_mode==2 && getCookie('APK_MODAL') == undefined) || window.apkpopup_mode==3) {

            if(window.apkpopup_mode==1) {
                setCookie('APK_MODAL_SHOWED',true, 1);
            }


            document.body.style.overflowY = 'hidden';
            document.getElementById("warning_apk").style.display = 'block';
        }
    }
}

function APKsuccessModalClose() {
    setCookie('APK_MODAL',true, 30);
    APKmodalClose();
}

function setCookie(name,value,days) {
    var expires = "";
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days*24*60*60*1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + value + expires + "; path=/";
}

function getCookie(name) {
    var matches = document.cookie.match(new RegExp(
        "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
    ));
    return matches ? decodeURIComponent(matches[1]) : undefined;
}

function toggle(idName) {
    var x = document.getElementById(idName);

    if (x.style.display === "none" ||  !x.style.display) {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }

}

document.onload = APKmodalOpen();