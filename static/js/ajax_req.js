// Access-Control-Allow-Origin: https://developer.mozilla.org
function send_data(key_pressed) {
	var data = document.getElementById("send_chat_txt_data").value;

	document.getElementById("send_chat_txt_data").value="";
	play_notification("human")
	display_chat_human(data);

	var doc=new XMLHttpRequest();
	var url="/process";
	// var url = "https://placementbot.pythonanywhere.com/process"
	var data="data="+data+"&key_pressed="+key_pressed;
	doc.open("POST",url,true);
	doc.setRequestHeader("Content-type","application/x-www-form-urlencoded");
	doc.onreadystatechange=function(){
	    if(doc.readyState==4 && doc.status==200){
	        var info=doc.responseText;
	        var obj = JSON.parse(info)
	        if(obj.answer!=null){
	        	display_chat_bot(obj.answer)
	        	play_notification("bot")
	        }
	        else if(obj.error!=null){
	        	alert(obj.error)
	        }
	    }
	}
	doc.send(data);
}
function show_hide_typing(show){
	if(show=="show"){
		document.getElementById("send_chat_txt_data").disabled=true;
		document.getElementById("typing_sending_thinking").style.display="block";
	}
	else{
		document.getElementById("send_chat_txt_data").disabled=false;
		document.getElementById("typing_sending_thinking").style.display="none";
	}
}
function display_chat_human(question){
	show_hide_typing("show")
	var chat_human = document.createElement("div");
	chat_human.setAttribute("class","chat_human");

	var chat_text_human = document.createElement("div");
	chat_text_human.setAttribute("class","chat_text_human");
	chat_text_human.innerHTML = question;

	var man_icon_chat_small = document.createElement("div");
	man_icon_chat_small.setAttribute("class","man_icon_chat_small");

	chat_human.appendChild(man_icon_chat_small)
	chat_human.appendChild(chat_text_human)
	
	document.getElementById("chat_body_main").appendChild(chat_human);
	scroll_chat_end();
}
function play_notification(person){
	if(person=="human"){
		var audio = new Audio('static/sounds/clearly.mp3');
		audio.play();
	}
	if(person=="bot"){
		var audio = new Audio('static/sounds/sharp.mp3');
		audio.play();	
	}
	
}
function display_chat_bot(answer){
	show_hide_typing("hide");
	var chat_bot = document.createElement("div");
	chat_bot.setAttribute("class","chat_bot");

	var chat_text_bot = document.createElement("div");
	chat_text_bot.setAttribute("class","chat_text_bot");
	chat_text_bot.innerHTML = answer;

	var bot_icon_chat_small = document.createElement("div");
	bot_icon_chat_small.setAttribute("class","bot_icon_chat_small");

	chat_bot.appendChild(chat_text_bot)
	chat_bot.appendChild(bot_icon_chat_small)

	document.getElementById("chat_body_main").appendChild(chat_bot);
	scroll_chat_end();
}
function scroll_chat_end(){
	var scroll_elem = document.getElementById('chat_body_main');
	scroll_elem.scrollTop = scroll_elem.scrollHeight;
}
function open_chat_box_small_screen(){
	document.getElementById('initial_chat_box').style.display = "block";
}
function hide_every_bot_ui(){
	document.getElementById('initial_chat_box').style.display = "none";
	document.getElementById('main_chat_chat_box').style.display = "none";
}
function display_hide_chat_box(){
	var full_name = document.getElementById('name_input_box').value;
	if(full_name.length>3){
		sessionStorage.setItem("user_full_name", full_name);
		document.getElementById('initial_chat_box').style.display = "none";
		document.getElementById('main_chat_chat_box').style.display = "block";
		document.getElementById('chat_start_info').innerHTML+="<br>"+sessionStorage.getItem("user_full_name");
	}
	else{
		document.getElementById('error_red_msg').style.display="block";
	}
	
}