$.ajax({
    url: "//sfu-nlp-class.appspot.com/leaderboard.js",
    //url: "leaderboard-fall2014.js",
    dataType: "script",
    beforeSend: function() {
        $('#loader').show();
    },
    timeout: 48000,
    error: function(x, t, m) {
        if (t == "timeout") {
            alert("The URL at sfu-nlp-class.appspot.com is not responding at the moment. Try again later.");
        } else {
            alert(t);
        }
    },
    success: function () {
        $('#loader').hide();
        // The current assignment number (0-indexed)
        var assignment_number = 3;

        // The maximum assignment number (0-indexed)
        var max_assignment_number = 3;

        var rows = "";
        var scoreranks = new Array();
        for (i = 0; i < data.length; i++) {
            var user = data[i][0];
            if (hidden_users[user]) {
                continue;
            }
            // if (user != 'default' && data[i][2] == "-inf") {
            //     continue;
            // }

            rows += '<tr id="' + user + '">';
            var prevscore = (i == 0) ? -1 : data[i-1][1+assignment_number];
            var score = data[i][1+assignment_number];
            if (score != prevscore) {
                scoreranks[score] = i;
                rows += '<td>' + (i+1) + '</td>';
            } else {
                rows += '<td></td>';
            }

            var rank = scoreranks[score];

            if (hidden_users[user]) {
              rows += "<td><i><strike>" + user + "</strike></i>";
              rows = rows + '</td>';
            } else {
              rows += '<td>' + user;
              // if (names[user]) {
              //     rows += ' (' + names[user] + ')';
              // }
              rows = rows + '</td>';
            }
            //for (j = 1; j < data[i].length; j++)
            for (j = 1; j < max_assignment_number + 2; j++)
                rows = rows + '<td class="score">' + data[i][j] + '</td>';
            //for (j = data[i].length; j < max_assignment_number + 2; j++)
             //   rows += '<td></td>';
            rows += "</tr>";
        }

        $('tbody:last').append(rows);
        $("td.score").addClass("text-right");
        $("#baseline").addClass('warning');
        $("#default").addClass('danger');
        $("#oracle").addClass('success');
        $('loading').hide();
    }
});
