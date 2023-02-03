function modalClose() {
    document.body.style.overflowY = 'auto';
    document.getElementById("warning").style.display = 'none';
}

function modalOpen() {

    if(window.popup_mode != undefined) {


        if ((window.popup_mode == 1 && getCookie('MODAL_SHOWED') == undefined) || (window.popup_mode==2 && getCookie('MODAL') == undefined) || window.popup_mode==3) {

            if(window.popup_mode==1) {
                setCookie('MODAL_SHOWED',true, 1);
            }


            document.body.style.overflowY = 'hidden';
            document.getElementById("warning").style.display = 'block';
        }
    }
}

function successModalClose() {
    setCookie('MODAL',true, 30);
    modalClose();
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

function showMobile() {
    document.getElementById("block-desktop").style.display = 'none';
    document.getElementById("block-mobile").style.display = 'block';

    document.getElementById("help-desktop").style.display = 'none';
    document.getElementById("help-mobile").style.display = 'block';
}

function showDesktop() {
    document.getElementById("block-mobile").style.display = 'none';
    document.getElementById("block-desktop").style.display = 'block';

    document.getElementById("help-mobile").style.display = 'none';
    document.getElementById("help-desktop").style.display = 'block';
}

function toggle(idName) {
    var x = document.getElementById(idName);

    if (x.style.display === "none" ||  !x.style.display) {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }

}

document.onload = modalOpen();