// script.js
function getAccessToken() {
    return '9d6f80249d6f80249d6f80244f9e77e22f99d6f9d6f8024fb20e6570520ea9118c9903f';
}

// id человека, чью стену хотим посмотреть.
function getOwnerId() {
    return 335591503;
    // return 15910946;
    // return 1;
}

function getDomain() {
    return 'extrawebdev';
}

// кол-во записей получаемых после запроса
function getCountOfNotes() {
    return 10;
}

// синглтон для хранения номера показанных записей (номера первой показанной записи)
var counterNote = (function () {
    var instance,
        counter = 0;

    var getCounter = function () {
        return counter;
    }

    var increaseCounter = function () {
        counter += 10;
    }

    var decreaseCounter = function () {
        counter -= 10;
    }

    var createInstance = function () {
        return {
            getCounter: getCounter,
            increaseCounter: increaseCounter,
            decreaseCounter: decreaseCounter
        }
    }

    return {
        getInstance: function () {
            if (!instance)
                return instance = createInstance();
            else
                return instance;
        }
    }
}());

$('#btnWall').on('click', loadWall);
$('#btnBack').on('click', back);
$('#btnForward').on('click', forward);

function getUrl(method, params) {
    if (!method) throw new Error('Укажите метод!');
    params = params || {};
    params['access_token'] = getAccessToken();
    return 'https://api.vk.com/method/' + method + '?' + $.param(params) + '&v=5.68';
}

function sendRequest(method, params, getData) {
    $.ajax({
        url: getUrl(method, params),
        method: 'GET',
        dataType: 'JSONP',
        success: getData
    });
}

function loadWall() {
    console.log(counterNote.getInstance().getCounter());
    sendRequest('wall.get', { count: getCountOfNotes(), owner_id: getOwnerId(), offset: counterNote.getInstance().getCounter() }, function getData(data) {
        showWall(data.response.items);
        console.log(data.response.items);
    });
}

function showWall(wall) {
    var html = '';
    for (var i = 0; i < wall.length; i++) {
        var note = wall[i];
        html += 
        '<li>' +
            '<div id="noteDiv">' +
                '<h4><a target="_blank" href="https://vk.com/id' + note.owner_id + '?w=wall' + note.owner_id + '_' + note.id + '">Перейти на запись</a></h4>' +
                '<br/>' + note.text + 
            '</div>';
        try {
            html += '<img src="' + note.attachments[0].photo.photo_604 + '"/>';
        } catch (Error) {}
        html += '</li>';
    }
    $('ul#wall').html(html);
}

function back() {
    if (counterNote.getInstance().getCounter() < 10) return;

    console.log(counterNote.getInstance().getCounter());
    counterNote.getInstance().decreaseCounter();
    loadWall();
}

function forward() {
    console.log(counterNote.getInstance().getCounter());
    counterNote.getInstance().increaseCounter();
    loadWall();
}

// плавный переход наверх при нажатии на кнопку Далее/Назад
$(function () {
    $(window).scroll(function () {
        if ($(this).scrollTop() != 0) {
            $('#navigation').fadeIn();
        } else {
            $('#navigation').fadeOut();
        }
    });

    $('#navigation').click(function () {
        $('body,html').animate({ scrollTop: 0 }, 800);
    });
});
