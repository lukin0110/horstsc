(function(window){
    var calendars = {};
    var gamesPrev = {};
    var gamesNext = {};
    var hours = 3*60*60*1000;

    function parseDate(datestr){
        //"20/04/13 15:45"
        var arr = datestr.split(" ");
        var arrdate = arr[0].split("/");
        var arrtime = arr[1].split(":");
        return new Date("20" + arrdate[2], parseInt(arrdate[1])-1, arrdate[0], arrtime[0], arrtime[1]);
    }

    function register(team, calendar){
        var current = new Date();
        var found = false;
        calendars[team] = calendar;

        for(var i=0;i<calendar.length;i++){
            var game = calendar[i];
            var date = parseDate(game[0]);
            game.unshift(date);

            if(!found && date.getTime() > (current.getTime()+hours)){
                gamesNext[team] = calendar[i];
                if(i>0){
                    gamesPrev[team] = calendar[i-1];
                }
                found = true;
            }
        }
    }

    function format(date, full){
        function inner(number){
            return number < 10 ? "0" + number : number;
        }
        var a=[];
        if(full){
            a.push(inner(date.getDate()));
            a.push('-');
            a.push(inner(date.getMonth() + 1));
            a.push('-' + date.getFullYear());
            a.push(" om ");
            a.push(inner(date.getHours()));
            a.push(":");
            a.push(inner(date.getMinutes()));
        } else {
            a.push(date.getDate() + '-' + (date.getMonth()+1));
            a.push(" ");
            a.push(inner(date.getHours()));
            a.push(":");
            a.push(inner(date.getMinutes()));
        }
        return a.join('');
    }

    function make(game, full){
        var a = [];
        var date = game[0];
        a.push('<tr>');
        a.push('<td><span class="label label-warning">' + format(date, full) + '</span></td>');

        if(game && game.length>3){
            a.push('<td class="right">');
            a.push(game[2]);
            a.push('</td><td class="score">');
            if(game.length>4){
                a.push(" <strong>");
                a.push(game[4]);
                a.push("-");
                a.push(game[5]);
                a.push("</strong> ");
            } else {
                a.push(" - ");
            }
            a.push('</td><td class="left">');
            a.push(game[3]);

        } else {
            a.push('<td colspan="3" class="score">vrij');
        }

        a.push("</td></tr>");
        return a.join("");
    }

    function makeCalendar(team){
        var calendar = calendars[team];
        var buf = [];

        for(var i=0; i<calendar.length; i++){
            buf.push(make(calendar[i], true));
        }
        return buf.join('');
    }


    if(!window.H){
        var exports = {
            make: make,
            makeCalendar: makeCalendar,
            register: register,
            prev: gamesPrev,
            next: gamesNext
        };

        window.H = exports;
    }
})(window);
