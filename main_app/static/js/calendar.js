let defaultTheme = 1;

let today = new Date();
const baseEvents = [
  {
    id: "imwyx6S",
    name: "Health Seminar",
    description: "Learn about maintaining a healthy lifestyle.",
    date: "01/12/2024",
    type: "event",
  },
  {
    id: "9jU6g6f",
    name: "Online Consultation",
    description: "Virtual consultation with health experts.",
    date: "02/01/2024",
    type: "event",
  },
  {
    id: "0g5G6ja",
    name: "Fitness Class",
    description: "Join us for a fun fitness session.",
    date: "03/15/2024",
    type: "event",
  },
  {
    id: "y2u7UaF",
    name: "Healthy Cooking Workshop",
    description: "Learn to prepare nutritious meals.",
    date: "05/20/2024",
    type: "event",
  }
];

function getRandomDate(start, end) {
  return new Date(start.getTime() + Math.random() * (end.getTime() - start.getTime()));
}

let events = [];

for (let i = 1; i <= 50; i++) {
  let startDate = getRandomDate(new Date(2024, 0, 1), new Date(2024, 5, 30));
  let baseEvent = baseEvents[i % baseEvents.length];

  let event = {
    id: baseEvent.id,
    name: baseEvent.name,
    description: baseEvent.description,
    date: `${startDate.getMonth() + 1}/${startDate.getDate()}/${startDate.getFullYear()}`,
    type: "health_event",
  };

  events.push(event);
}

let active_events = [];

let week_date = [];

let curAdd, curRmv;

function getRandom(a) {
	return Math.floor(Math.random() * a);
}

function getWeeksInMonth(a, b) {
	let c = [],
		d = new Date(b, a, 1),
		e = new Date(b, a + 1, 0),
		f = e.getDate();
	let g = 1;
	let h = 7 - d.getDay();
	while (g <= f) {
		c.push({
			start: g,
			end: h
		});
		g = h + 1;
		h += 7;
		if (h > f) h = f;
	}
	return c;
}

week_date = getWeeksInMonth(today.getMonth(), today.getFullYear())[2];

$(document).ready(function() {
	$("#demoEvoCalendar").evoCalendar({
		format: "MM dd, yyyy",
		titleFormat: "MM",
		calendarEvents: [{
			id: "d8jai7s",
			name: "Marketing and Management",
			description: "Admin's Note, Thank you for using our Application! :)",
			date: "February/18/2024",
			type: "birthday",
			everyYear: !0
		}, {
			id: "in8bha4",
			name: "Blog Posts",
			description: "Create Posts to be Displayed on the Website",
			date: today,
			type: "event"
		}, {
			id: "in8bha4",
			name: "Consultation",
			description: "Perform a self-diagnosis using our Disease Prediction Tool and schedule a consultation with our specialized medical practitioners.",
			date: today,
			type: "event"
		}, {
			id: "d8jai7s",
			name: "Nemisa Datathon",
			description: "Join us for the Nemisa Datathon Project Demo in East London.",
			date: "02/21/2024",
			type: "holiday",
		}, {
			id: "d8jai7s",
			name: "Nemisa Datathon",
			description: "Join us for the Nemisa Datathon Project Demo in East London.",
			date: "02/22/2024",
			type: "holiday",
		}, {
			id: "d8jai7s",
			name: "Nemisa Datathon",
			description: "Join us for the Nemisa Datathon Project Demo in East London.",
			date: "02/23/2024",
			type: "holiday",
		}, {
			id: "d8jai7s",
			name: "Nemisa Datathon",
			description: "Join us for the Nemisa Datathon Project Demo in East London.",
			date: "02/24/2024",
			type: "holiday",
		}, ].concat(events)
	});
	$("[data-set-theme]").click(function(b) {
		a(b.target);
	});
	$("#addBtn").click(function(a) {
		curAdd = getRandom(events.length);
		$("#demoEvoCalendar").evoCalendar("addCalendarEvent", events[curAdd]);
		active_events.push(events[curAdd]);
		events.splice(curAdd, 1);
		if (0 === events.length) a.target.disabled = !0;
		if (active_events.length > 0) $("#removeBtn").prop("disabled", !1);
	});
	$("#removeBtn").click(function(a) {
		curRmv = getRandom(active_events.length);
		$("#demoEvoCalendar").evoCalendar("removeCalendarEvent", active_events[curRmv].id);
		events.push(active_events[curRmv]);
		active_events.splice(curRmv, 1);
		if (0 === active_events.length) a.target.disabled = !0;
		if (events.length > 0) $("#addBtn").prop("disabled", !1);
	});
	a($("[data-set-theme]")[defaultTheme]);

	function a(a) {
		let b = a.dataset.setTheme;
		$("[data-set-theme]").removeClass("active");
		$(a).addClass("active");
		$("#demoEvoCalendar").evoCalendar("setTheme", b);
	}
	let b = getRandom($("[data-settings]").length);
	let c = $("[data-settings]")[b];
	let d = getRandom($("[data-method]").length);
	let e = $("[data-method]")[d];
	let f = getRandom($("[data-event]").length);
	let g = $("[data-event]")[f];
	showSettingsSample($(c).data().settings);
	showMethodSample($(e).data().method);
	showEventSample($(g).data().event);
	$("[data-settings]").on("click", function(a) {
		let b = $(a.target).closest("[data-settings]");
		let c = b.data().settings;
		showSettingsSample(c);
	});
	$("[data-method]").on("click", function(a) {
		let b = $(a.target).closest("[data-method]");
		let c = b.data().method;
		showMethodSample(c);
	});
	$("[data-event]").on("click", function(a) {
		let b = $(a.target).closest("[data-event]");
		let c = b.data().event;
		showEventSample(c);
	});
});

function showSettingsSample(a) {
	let b = $("#event-settings");
	let c;
	switch (a) {
		case "theme":
			c = '<br><span class="green">// theme</span><br>' + '$(<span class="red">\'#calendar\'</span>).<span class="yellow">evoCalendar</span>({<br>' + "&#8194;&#8194;&#8194;&#8194;&#8194;<span class=\"blue\">'theme'</span>: <span class=\"red\">'Theme Name'</span><br>" + "});" + "<br> ";
			break;

		case "language":
			c = '<br><span class="green">// language</span><br>' + '$(<span class="red">\'#calendar\'</span>).<span class="yellow">evoCalendar</span>({<br>' + "&#8194;&#8194;&#8194;&#8194;&#8194;<span class=\"blue\">'language'</span>: <span class=\"red\">'en'</span><br>" + '&#8194;&#8194;&#8194;&#8194;&#8194;<span class="green">// Supported language: en, es, de..</span><br>' + "});" + "<br> ";
			break;

		case "format":
			c = '<br><span class="green">// format</span><br>' + '$(<span class="red">\'#calendar\'</span>).<span class="yellow">evoCalendar</span>({<br>' + "&#8194;&#8194;&#8194;&#8194;&#8194;<span class=\"blue\">'format'</span>: <span class=\"red\">'MM dd, yyyy'</span><br>" + '&#8194;&#8194;&#8194;&#8194;&#8194;<span class="green">// some browsers doesn\'t support other format, so...</span><br>' + "});" + "<br> ";
			break;

		case "titleFormat":
			c = '<br><span class="green">// titleFormat</span><br>' + '$(<span class="red">\'#calendar\'</span>).<span class="yellow">evoCalendar</span>({<br>' + "&#8194;&#8194;&#8194;&#8194;&#8194;<span class=\"blue\">'titleFormat'</span>: <span class=\"red\">'MM'</span><br>" + "});" + "<br> ";
			break;

		case "eventHeaderFormat":
			c = '<br><span class="green">// eventHeaderFormat</span><br>' + '$(<span class="red">\'#calendar\'</span>).<span class="yellow">evoCalendar</span>({<br>' + "&#8194;&#8194;&#8194;&#8194;&#8194;<span class=\"blue\">'eventHeaderFormat'</span>: <span class=\"red\">'MM dd'</span><br>" + "});" + "<br> ";
			break;

		case "firstDayOfWeek":
			c = '<br><span class="green">// firstDayOfWeek</span><br>' + '$(<span class="red">\'#calendar\'</span>).<span class="yellow">evoCalendar</span>({<br>' + '&#8194;&#8194;&#8194;&#8194;&#8194;<span class="blue">\'firstDayOfWeek\'</span>: <span class="red">0</span> <span class="green">// Sun</span><br>' + '&#8194;&#8194;&#8194;&#8194;&#8194;<span class="green">// 0-6 (Sun-Sat)</span><br>' + "});" + "<br> ";
			break;

		case "todayHighlight":
			c = '<br><span class="green">// todayHighlight</span><br>' + '$(<span class="red">\'#calendar\'</span>).<span class="yellow">evoCalendar</span>({<br>' + '&#8194;&#8194;&#8194;&#8194;&#8194;<span class="blue">\'todayHighlight\'</span>: <span class="blue">true</span><br>' + "});" + "<br> ";
			break;

		case "sidebarDisplayDefault":
			c = '<br><span class="green">// sidebarDisplayDefault</span><br>' + '$(<span class="red">\'#calendar\'</span>).<span class="yellow">evoCalendar</span>({<br>' + '&#8194;&#8194;&#8194;&#8194;&#8194;<span class="blue">\'sidebarDisplayDefault\'</span>: <span class="blue">false</span><br>' + "});" + "<br> ";
			break;

		case "sidebarToggler":
			c = '<br><span class="green">// sidebarToggler</span><br>' + '$(<span class="red">\'#calendar\'</span>).<span class="yellow">evoCalendar</span>({<br>' + '&#8194;&#8194;&#8194;&#8194;&#8194;<span class="blue">\'sidebarToggler\'</span>: <span class="blue">false</span><br>' + "});" + "<br> ";
			break;

		case "eventDisplayDefault":
			c = '<br><span class="green">// eventDisplayDefault</span><br>' + '$(<span class="red">\'#calendar\'</span>).<span class="yellow">evoCalendar</span>({<br>' + '&#8194;&#8194;&#8194;&#8194;&#8194;<span class="blue">\'eventDisplayDefault\'</span>: <span class="blue">false</span><br>' + "});" + "<br> ";
			break;

		case "eventListToggler":
			c = '<br><span class="green">// eventListToggler</span><br>' + '$(<span class="red">\'#calendar\'</span>).<span class="yellow">evoCalendar</span>({<br>' + '&#8194;&#8194;&#8194;&#8194;&#8194;<span class="blue">\'eventListToggler\'</span>: <span class="blue">false</span><br>' + "});" + "<br> ";
			break;

		case "calendarEvents":
			c = '<br><span class="green">// calendarEvents</span><br>' + '$(<span class="red">\'#calendar\'</span>).<span class="yellow">evoCalendar</span>(<span class="blue">\'calendarEvents\'</span>, {<br>' + "&#8194;&#8194;&#8194;&#8194;&#8194;<span class=\"blue\">'calendarEvents'</span>: [<br>" + "&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;{<br>" + '&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;<span class="blue">id</span>: <span class="red">\'4hducye\'</span>, <span class="green">// Event\'s id (required, for removing event)</span><br>' + '&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;<span class="blue">description</span>: <span class="red">\'Lorem ipsum dolor sit amet..\'</span>, <span class="green">// Description of event (optional)</span><br>' + '&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;<span class="blue">badge</span>: <span class="red">\'1-day event\'</span>, <span class="green">// Event badge (optional)</span><br>' + '&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;<span class="blue">date</span>: <span class="blue">new</span> <span class="yellow">Date</span>(), <span class="green">// Date of event</span><br>' + '&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;<span class="blue">type</span>: <span class="red">\'holiday\'</span>, <span class="green">// Type of event (event|holiday|birthday)</span><br>' + '&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;<span class="blue">color</span>: <span class="red">\'#63d867\'</span>, <span class="green">// Event custom color (optional)</span><br>' + '&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;<span class="blue">everyYear</span>: <span class="blue">true</span> <span class="green">// Event is every year (optional)</span><br>' + "&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;}<br>" + "&#8194;&#8194;&#8194;&#8194;&#8194;]<br>" + "});" + "<br> ";
	}
	$("[data-settings]").removeClass("active");
	$('[data-settings="' + a + '"]').addClass("active");
	b.html(c);
}

function showMethodSample(a) {
	let b = $("#method-code");
	let c;
	switch (a) {
		case "setTheme":
			c = '<br><span class="green">// setTheme</span><br>' + '$(<span class="red">\'#calendar\'</span>).<span class="yellow">evoCalendar</span>(<span class="blue">\'setTheme\'</span>, <span class="red">\'Theme Name\'</span>);' + "<br> ";
			break;

		case "toggleSidebar":
			c = '<br><span class="green">// toggleSidebar</span><br>' + '$(<span class="red">\'#calendar\'</span>).<span class="yellow">evoCalendar</span>(<span class="blue">\'toggleSidebar\'</span>);' + "<br> " + '<br><span class="green">// open sidebar</span><br>' + '$(<span class="red">\'#calendar\'</span>).<span class="yellow">evoCalendar</span>(<span class="blue">\'toggleSidebar\'</span>, <span class="blue">true</span>);' + "<br> ";
			break;

		case "toggleEventList":
			c = '<br><span class="green">// toggleEventList</span><br>' + '$(<span class="red">\'#calendar\'</span>).<span class="yellow">evoCalendar</span>(<span class="blue">\'toggleEventList\'</span>);' + "<br> " + '<br><span class="green">// close event list</span><br>' + '$(<span class="red">\'#calendar\'</span>).<span class="yellow">evoCalendar</span>(<span class="blue">\'toggleEventList\'</span>, <span class="blue">false</span>);' + "<br> ";
			break;

		case "getActiveDate":
			c = '<br><span class="green">// getActiveDate</span><br>' + '<span class="red">let</span> <span class="orange">active_date</span> = $(<span class="red">\'#calendar\'</span>).<span class="yellow">evoCalendar</span>(<span class="blue">\'getActiveDate\'</span>);' + "<br> ";
			break;

		case "getActiveEvents":
			c = '<br><span class="green">// getActiveEvents</span><br>' + '<span class="red">let</span> <span class="orange">active_events</span> = $(<span class="red">\'#calendar\'</span>).<span class="yellow">evoCalendar</span>(<span class="blue">\'getActiveEvents\'</span>);' + "<br> ";
			break;

		case "selectYear":
			c = '<br><span class="green">// selectYear</span><br>' + '$(<span class="red">\'#calendar\'</span>).<span class="yellow">evoCalendar</span>(<span class="blue">\'selectYear\'</span>, <span class="red">2021</span>);' + "<br> ";
			break;

		case "selectMonth":
			c = '<br><span class="green">// selectMonth</span><br>' + '$(<span class="red">\'#calendar\'</span>).<span class="yellow">evoCalendar</span>(<span class="blue">\'selectMonth\'</span>, <span class="red">1</span>); <span class="green">// february</span>' + "<br> ";
			break;

		case "selectDate":
			c = '<br><span class="green">// selectDate</span><br>' + '$(<span class="red">\'#calendar\'</span>).<span class="yellow">evoCalendar</span>(<span class="blue">\'selectDate\'</span>, <span class="red">\'February 15, 2020\'</span>);' + "<br> ";
			break;

		case "addCalendarEvent":
			c = '<br><span class="green">// addCalendarEvent</span><br>' + '$(<span class="red">\'#calendar\'</span>).<span class="yellow">evoCalendar</span>(<span class="blue">\'addCalendarEvent\'</span>, {<br>' + '&#8194;&#8194;&#8194;&#8194;&#8194;<span class="blue">id</span>: <span class="red">\'kNybja6\'</span>,<br>' + '&#8194;&#8194;&#8194;&#8194;&#8194;<span class="blue">name</span>: <span class="red">\'Mom\\\'s Birthday\'</span>,<br>' + '&#8194;&#8194;&#8194;&#8194;&#8194;<span class="blue">description</span>: <span class="red">\'Lorem ipsum dolor sit..\'</span>,<br>' + '&#8194;&#8194;&#8194;&#8194;&#8194;<span class="blue">date</span>: <span class="red">\'May 27, 2020\'</span>,<br>' + '&#8194;&#8194;&#8194;&#8194;&#8194;<span class="blue">type</span>: <span class="red">\'birthday\'</span><br>' + "});" + '<br><span class="green">// add multiple events</span><br>' + '$(<span class="red">\'#calendar\'</span>).<span class="yellow">evoCalendar</span>(<span class="blue">\'addCalendarEvent\'</span>, [<br>' + "&#8194;&#8194;&#8194;&#8194;&#8194;{<br>" + '&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;<span class="blue">id</span>: <span class="red">\'kNybja6\'</span>,<br>' + '&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;<span class="blue">name</span>: <span class="red">\'Mom\\\'s Birthday\'</span>,<br>' + '&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;<span class="blue">date</span>: <span class="red">\'May 27, 1965\'</span>,<br>' + '&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;<span class="blue">type</span>: <span class="red">\'birthday\'</span>,<br>' + '&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;<span class="blue">everyYear</span>: <span class="blue">true</span> <span class="green">// optional</span><br>' + "&#8194;&#8194;&#8194;&#8194;&#8194;},<br>" + "&#8194;&#8194;&#8194;&#8194;&#8194;{<br>" + '&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;<span class="blue">id</span>: <span class="red">\'asDf87L\'</span>,<br>' + '&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;<span class="blue">name</span>: <span class="red">\'Graduation Day!\'</span>,<br>' + '&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;<span class="blue">date</span>: <span class="red">\'March 21, 2020\'</span>,<br>' + '&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;<span class="blue">type</span>: <span class="red">\'event\'</span><br>' + "&#8194;&#8194;&#8194;&#8194;&#8194;}<br>" + "]);" + "<br> ";
			break;

		case "removeCalendarEvent":
			c = '<br><span class="green">// removeCalendarEvent</span><br>' + '$(<span class="red">\'#calendar\'</span>).<span class="yellow">evoCalendar</span>(<span class="blue">\'removeCalendarEvent\'</span>, <span class="red">\'kNybja6\'</span>);' + "<br> " + '<br><span class="green">// delete multiple event</span><br>' + '$(<span class="red">\'#calendar\'</span>).<span class="yellow">evoCalendar</span>(<span class="blue">\'removeCalendarEvent\'</span>, [<span class="red">\'kNybja6\'</span>, <span class="red">\'asDf87L\'</span>]);' + "<br> ";
			break;

		case "destroy":
			c = '<br><span class="green">// destroy</span><br>' + '$(<span class="red">\'#calendar\'</span>).<span class="yellow">evoCalendar</span>(<span class="blue">\'destroy\'</span>);' + "<br> ";
	}
	$("[data-method]").removeClass("active");
	$('[data-method="' + a + '"]').addClass("active");
	b.html(c);
}

function showEventSample(a) {
	let b = $("#event-code");
	let c;
	switch (a) {
		case "selectDate":
			c = '<br><span class="green">// selectDate</span><br>' + '$(<span class="red">\'#calendar\'</span>).<span class="yellow">on</span>(<span class="blue">\'selectDate\'</span>, <span class="blue">function</span>(<span class="yellow">event</span>, <span class="yellow">newDate</span>, <span class="yellow">oldDate</span>) {<br>' + '&#8194;&#8194;&#8194;&#8194;&#8194;<span class="green">// code here...</span><br>' + "});" + "<br> ";
			break;

		case "selectEvent":
			c = '<br><span class="green">// selectEvent</span><br>' + '$(<span class="red">\'#calendar\'</span>).<span class="yellow">on</span>(<span class="blue">\'selectEvent\'</span>, <span class="blue">function</span>(<span class="yellow">event</span>, <span class="yellow">activeEvent</span>) {<br>' + '&#8194;&#8194;&#8194;&#8194;&#8194;<span class="green">// code here...</span><br>' + "});" + "<br> ";
			break;

		case "selectMonth":
			c = '<br><span class="green">// selectMonth</span><br>' + '$(<span class="red">\'#calendar\'</span>).<span class="yellow">on</span>(<span class="blue">\'selectMonth\'</span>, <span class="blue">function</span>(<span class="yellow">event</span>, <span class="yellow">activeMonth</span>, <span class="yellow">monthIndex</span>) {<br>' + '&#8194;&#8194;&#8194;&#8194;&#8194;<span class="green">// code here...</span><br>' + "});" + "<br> ";
			break;

		case "selectYear":
			c = '<br><span class="green">// selectYear</span><br>' + '$(<span class="red">\'#calendar\'</span>).<span class="yellow">on</span>(<span class="blue">\'selectYear\'</span>, <span class="blue">function</span>(<span class="yellow">event</span>, <span class="yellow">activeYear</span>) {<br>' + '&#8194;&#8194;&#8194;&#8194;&#8194;<span class="green">// code here...</span><br>' + "});" + "<br> ";
			break;

		case "destroy":
			c = '<br><span class="green">// destroy</span><br>' + '$(<span class="red">\'#calendar\'</span>).<span class="yellow">on</span>(<span class="blue">\'destroy\'</span>, <span class="blue">function</span>(<span class="yellow">event</span>, <span class="yellow">evoCalendar</span>) {<br>' + '&#8194;&#8194;&#8194;&#8194;&#8194;<span class="green">// code here...</span><br>' + "});" + "<br> ";
	}
	$("[data-event]").removeClass("active");
	$('[data-event="' + a + '"]').addClass("active");
	b.html(c);
}

$('[data-go*="#"]').on("click", function(a) {
	a.preventDefault();
	let b = $(this).data().go;
	if ("#top" === b) {
		$("html, body").animate({
			scrollTop: 0
		}, 500);
		return;
	} else var c = $(b)[0].offsetTop - $("header")[0].offsetHeight - 10;
    
	$("html, body").animate({
		scrollTop: c
	}, 500);
});
