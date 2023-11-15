

window.onbeforeprint = function () {
    alert("not show");
    document.body.innerHTML = '<div class="watermark"><p>bookhut.ir</p></div>';
    return false;
    window.close();
}

document.addEventListener('keydown', function (e) {
    if (e.ctrlKey && e.key == 'P') {
        document.body.innerHTML = '<div class="watermark"><p>bookhut.ir</p></div>';
        return false;
    }
});




function set_cookie(cname, cvalue, exdeys) {
    const d = new Date();
    d.setTime(d.getTime() + (exdeys * 24 * 60 * 60 * 1000));
    let expires = "expires=" + d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

function get_cookie(cname) {
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for (let i = 0; i < ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

function getSlug() {
    let URL = window.location.pathname;
    let URL_LENGHT = URL.split('/');
    let urlCount = URL_LENGHT.length;
    let result = URL_LENGHT[urlCount - 1];
    return result;
}

function getScrolls() {
    let domScroll = document.documentElement.scrollTop;
    let slug = getSlug();
    set_cookie(slug, domScroll, 365);
}

function getScrollsOld() {
    let slug = getSlug();
    let cook = get_cookie(slug);
    if (cook != null || cook != '') {
        set_cookie(slug, cook, 365);
        document.documentElement.scrollTop = cook;
    }
}


window.onload = function () {
    getScrollsOld();
}



window.onscroll = function () {
    getScrolls();
}







