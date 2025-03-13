$(document).ready(function() {
    $('#recommendBtn').click(function() {
        const mood = $('#moodSelect').val();
        $.ajax({
            url: '/get_songs',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ mood: mood }),
            success: function(songs) {
                $('#songList').empty();
                songs.forEach(function(song) {
                    $('#songList').append(`<li class="list-group-item">${song[0]} by ${song[1]}</li>`);
                });
            }
        });
    });
});