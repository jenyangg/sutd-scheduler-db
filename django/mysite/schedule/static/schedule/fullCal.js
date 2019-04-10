$(document).ready(function(){

        // $('.selectpicker').selectpicker();

        $('#calendar').fullCalendar({
            //hiddenDays:[0,6], same as below

            weekends: false,
            header : {
                left: "month,agendaWeek,agendaDay", //space leaves a gap between buttons
                center: "title",
                right:"today, prev,next"
            },
            aspectRatio:1.5,
            defaultView: 'agendaWeek',
            // themeSystem: 'bootstrap4',
            allDaySlot: false,
            height: 'auto',
            timezone: 'Asia/Singapore',
            /* Min and Max time on calendar */
            minTime: "08:00:00",
            maxTime: "20:00:00",
            events:[
                {
                    title: "Elements of Software Construction",
                    start: "2019-02-25 10:00", //YYYY-MM-DD
                    end: "2019-02-25 11:30",
                    description: "Prof",
                    location: "LT"
                },
                {
                    title: "Probs and Stats",
                    start: "2019-04-01 08:00",
                    end: "2019-04-01 09:40",
                    description: "Prof",
                    location: "CC13"
                }
            ],
            color: 'yellow',
            textColor: 'black',

            eventRender: function(objEvent, element, view) {
                if (view.name === "agendaWeek" || view.name === "agendaDay"){
                 element.find(".fc-content").append(objEvent.location + "</br>" + objEvent.description);
                 //element.find(".fc-title").empty().append('<div class="fc-title"><b>Probs and Stats<b></div>')
                }},

            eventAfterAllRender: function (view, element) {
                //The title isn't rendered until after this callback, so we need to use a timeout.
                if(view.type === "agendaWeek"){
                    // tried to use flex to align, didn't work out well
                    window.setTimeout(function(){
                        $("#calendar").find('#calendar-additions').remove();
                        $("#calendar").find('.fc-toolbar').append(
                            "<div id='calendar-additions'>"+
                            "<li><select class='selectpicker' multiple data-actions-box='true' title='Filter'>"+
                            "<option>Course 1</option>"+
                            "<option>Course 2</option>"+
                            "</select></li>"+
                            "<li><button class='button-submit'>&#x21B5;</button></li>"+
                            "<li><button id='export-button'>"+
                            '<i class="far fa-share-square"></i>'+
                            "<p id='export_text'>Export</p>"+
                            "</button></li>"+
                            "<div id='blank_row'></div>"+
                            "</div>"
                        );
                        $('.selectpicker').selectpicker();
                    },0);
                }
            },
        });
    });
