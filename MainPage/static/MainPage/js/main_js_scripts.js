/*===mobpop_on/off================================================*/
var mob_menu_pop=document.getElementById('mob_menu_pop');

function burger_click() {
     mob_menu_pop.style.display = "block";
}

function menu_pop_up_exit_click() {
    mob_menu_pop.style.display = "none";
}

/*=подсвет пунктов меню при скроле===================================*/
function nonstop_window_y_offset() {
    var viewport_h=window.innerHeight;
    var screen_line=elem_coordinates().window_y_offset;
    var menu_line=elem_coordinates().window_y_offset+header_height_func();
    var menu_line_nz=menu_line+1;
    var about_y=elem_coordinates().about_y;
    var price_y=elem_coordinates().price_y;
    var quality_y=elem_coordinates().quality_y;
    var contacts_y=elem_coordinates().contacts_y;
    var footer_y=elem_coordinates().footer_y;

    if (0<menu_line_nz && menu_line_nz<about_y){menu_item_style_off();}
    if (about_y<menu_line_nz && menu_line_nz<price_y){menu_item_style_handler(0);}
    if (price_y<menu_line_nz && menu_line_nz<quality_y){menu_item_style_handler(1);}
    if (quality_y<menu_line_nz && menu_line_nz<contacts_y){menu_item_style_handler(2);}
    if (contacts_y<menu_line_nz && menu_line_nz<footer_y){menu_item_style_handler(3);}
    if (screen_line+viewport_h+1>footer_y){menu_item_style_handler(4);}

}
setInterval(nonstop_window_y_offset, 100);

function menu_item_style_handler (num){
    menu_item_style_off();
    menu_item_style_on(num);
}

function menu_item_style_on(num) {
    var menu_mas_menu_item=document.getElementsByClassName('menu_item');
    var menu_mas_menu_link=document.getElementsByClassName('menu_link');
    menu_mas_menu_item[num].style.transform='scale(1.05)';
    menu_mas_menu_link[num].style.color='#608883';
}

function menu_item_style_off() {
    var menu_mas_menu_item = document.getElementsByClassName('menu_item');
    var menu_mas_menu_link = document.getElementsByClassName('menu_link');
    for (var i = 0; i < menu_mas_menu_item.length; i++) {
        menu_mas_menu_item[i].style.transform = '';
        menu_mas_menu_link[i].style.color = '';
    }
}

/*===anchors=========================================================*/
function elem_coordinates() {
    var window_y_offset = window.pageYOffset;
    var banner_y = document.getElementById('banner_id').getBoundingClientRect().top + window_y_offset;
    var about_y = document.getElementById('about_us_id').getBoundingClientRect().top + window_y_offset;
    var price_y = document.getElementById('price_wrap_id').getBoundingClientRect().top + window_y_offset;
    var quality_y = document.getElementById('quality_id').getBoundingClientRect().top + window_y_offset;
    var contacts_y = document.getElementById('contacts_id').getBoundingClientRect().top + window_y_offset;
    var footer_y = document.getElementById('footer_id').getBoundingClientRect().bottom + window_y_offset;

    return {
        window_y_offset:window_y_offset,
        banner_y:banner_y,
        about_y:about_y,
        price_y:price_y,
        quality_y:quality_y,
        contacts_y:contacts_y,
        footer_y:footer_y
    }
}

function header_height_func (){
    var header = document.getElementById('header_id');
    var header_height = header.getBoundingClientRect().height || (header.getBoundingClientRect().bottom - header.getBoundingClientRect().top);
    return header_height;
}

function scroll(y_coord){
    var broser = window.navigator.userAgent;

    if (broser.indexOf('Edge')==-1){
       /* console.log('Not IE');*/
        scrollTo({top: (y_coord-header_height_func()), behavior:"smooth"});
    }
    else {
        /*console.log('IE');*//*долбоёб не понимает scrollTo options*/
        scrollTo(0,(y_coord-header_height_func()));
    }
}

function scroll_to_banner(){
    scroll(elem_coordinates().banner_y);
}
function scroll_to_about(){
    scroll(elem_coordinates().about_y);
}
function scroll_to_price(){
    scroll(elem_coordinates().price_y);
}
function scroll_to_quality(){
    scroll(elem_coordinates().quality_y);
}
function scroll_to_contacts(){
    scroll(elem_coordinates().contacts_y);
}
function scroll_to_footer(){
    scroll(elem_coordinates().footer_y);
}

function scroll_to_banner_mob(){
    mob_menu_pop.style.display = "none";
    scroll(elem_coordinates().banner_y);
}
function scroll_to_about_mob(){
    mob_menu_pop.style.display = "none";
    scroll(elem_coordinates().about_y);
}
function scroll_to_price_mob(){
    mob_menu_pop.style.display = "none";
    scroll(elem_coordinates().price_y);
}
function scroll_to_quality_mob(){
    mob_menu_pop.style.display = "none";
    scroll(elem_coordinates().quality_y);
}
function scroll_to_contacts_mob(){
    mob_menu_pop.style.display = "none";
    scroll(elem_coordinates().contacts_y);
}
function scroll_to_footer_mob(){
    mob_menu_pop.style.display = "none";
    scroll(elem_coordinates().footer_y);
}

/*===TelMask=============================================================*/
function focuss (event) {
    if (event.target.value=='') {
        event.target.value='+38 (';
    }
    else {event.target.value=event.target.value;}
}
function focuss_out (event) {
    if (event.target.value=='+38 (') {event.target.value='';}
    else {event.target.value=event.target.value;}
}
function keypres_func (event){
    if (event.target.value=='') { event.target.value='+38 (';}
    var digits_mas=['0','1','2','3','4','5','6','7','8','9'];
    if ((event.key in digits_mas)!=true) {
        return false;
        }
    if (event.target.value.length==8) { event.target.value+=') ';}
    if (event.target.value.length==13) { event.target.value+='-';}
    if (event.target.value.length==16) { event.target.value+='-';}
    if (event.target.value.length>18) {return false;}
}

function keydown_func (event) {
    if (event.target.value == '+38 (' && (event.key == 'Backspace' || event.key == 'Delete' || event.key == 'ArrowLeft')) {
        return false;
    }
}
var phone=document.getElementsByName('telephone');

for (var i in phone) {
    phone[i].onfocus = focuss;
}
for (var i in phone) {
    phone[i].onblur = focuss_out;
}
for (var i in phone) {
    phone[i].onkeypress = keypres_func;
}
for (var i in phone) {
    phone[i].onkeydown = keydown_func;
}


/*==alerts==============================================================*/

var message_btn=document.getElementById('message_btn_id');
var call_btn=document.getElementById('call_btn_id');

function normal_boder (element){
   element.style.borderBottomColor = '#ffffff';
   element.style.borderLeftColor = '#ffffff';
}

function alert_boder (element){
   element.style.borderBottomColor = '#e1433f';
   element.style.borderLeftColor = '#e1433f';
}

function tel_validator(element) {
    var regexp_tel= new RegExp("\\+38\\s+\\(\\d\\d\\d\\)\\s+\\d\\d\\d\\-\\d\\d\\-\\d\\d");
    if (element.value.search(regexp_tel)==0){ normal_boder(element);return true;}
    else { alert_boder(element); return false;}
}

function mail_validator(element) {
    var regexp_email= new RegExp("^[A-Za-z0-9._-]+@[A-Za-z]+\\.[a-z]+$");
    if (element.value.search(regexp_email)==0 || element.value=='' ){ normal_boder(element); return true;}
    else {alert_boder(element); return false;}
}

function char_field_validator(element) {
    if (element.value!=''){ normal_boder(element);  return true;}
    else {alert_boder(element); return false;}
}


function value_trim(element) {
    var tr_value=element.value.trim();
    return tr_value;
}


var message_btn_var=function message_btn_func(event){
    /*получаем елементы инпутов*/
    var name_input=document.getElementById('name');
    var phone_input=document.getElementById('phone');
    var email_input=document.getElementById('email');
    var text_message_input=document.getElementById('text_message');
    /*получаем елемент токена*/
    var csrfmiddlewaretokens=document.getElementsByName('csrfmiddlewaretoken');
    var csrfmiddlewaretoken=csrfmiddlewaretokens[0];

    /*убираем в значениях пробелы вначале и в конце*/
    name_input.value=value_trim(name_input);
    phone_input.value=value_trim(phone_input);
    email_input.value=value_trim(email_input)+'.';  /*(костыль)без добавления какогото символа в конце трим */
    email_input.value=email_input.value.slice(0,-1); /*не хочет работать с инпутом мыла; добавляем '.' и удаляем ее*/
    text_message_input.value=value_trim(text_message_input);

    /*формируем обьект для передачи в аджакс (в виде json)*/
    var params_obj={
            'name':name_input.value,
            'telephone':phone_input.value,
            'email':email_input.value,
            'text_message':text_message_input.value
        }
    var params_obj_json=JSON.stringify(params_obj);

    /*валидируем значения*/
    var name_ok=char_field_validator(name_input);
    var tel_ok=tel_validator(phone_input);
    var email_ok=mail_validator(email_input);
    var text_message_ok=char_field_validator(text_message_input);

    /*если всё ок - вызываем отправку аджаксом. (обязательно передать токен)*/
    if (name_ok && tel_ok && email_ok && text_message_ok ){
        event.preventDefault();
        ajaxPost_for_message_btn(params_obj_json, csrfmiddlewaretoken.value);
        return true;
    }
    else {
        event.preventDefault();
        return false;
    }
}


function url_encode(string) {
    var encode_string;
    encode_string=string.replace('+','%2B');
    encode_string=encode_string.replace(new RegExp(' ', 'g'),'+'); /*все пробелы а не только первый*/
    encode_string=encode_string.replace('(','%28');
    encode_string=encode_string.replace(')','%29');
    return encode_string;
}

function call_btn_daytime_validator() {
    var now=new Date();
    var now_hour=now.getHours();
    var now_dayweek=now.getDay();
    var from_hour=10, to_hour=19; /*менять и на бэке*/
    var valid_dayweek_mas=[0,1,2,3,4,5,6];

    if (from_hour<=now_hour && now_hour<to_hour && now_dayweek in valid_dayweek_mas) {
        return true
    }
    else {
        success_pop_show('call btn validator');
        return false
    }
}

var call_btn_var=function call_btn_func(event){
    var call_phone_input=document.getElementById('call_phone');

    if (call_btn_daytime_validator()==false){
        console.log('call btn BREAK');
        event.preventDefault();
        call_phone_input.value='';
        return false
    }
    console.log('call btn go on!');

    call_phone_input.value=value_trim(call_phone_input);

    var tel_ok=tel_validator(call_phone_input);

    var params = 'telephone='+url_encode(call_phone_input.value);

    if (tel_ok){
        console.log('recall OK');
        event.preventDefault();
        ajaxGet_for_call_btn(params);
        return true;
    }
    else {
        event.preventDefault();
        console.log('recall NOT OK');
        return false;
    }
}

function ajaxPost_for_message_btn (params, token){
    var name_input=document.getElementById('name');
    var phone_input=document.getElementById('phone');
    var email_input=document.getElementById('email');
    var text_message_input=document.getElementById('text_message');

    var request = new XMLHttpRequest();

    request.open('POST', '/', true);

    request.onreadystatechange=function(){
        if (request.readyState==4 && request.status==200){
            console.log('Вернулся ответ! message');
        }

    }

    request.setRequestHeader('Content-Type', 'application/json');
    request.setRequestHeader('X-CSRFToken', token);
    request.setRequestHeader('X-REQUESTED-WITH', 'XMLHttpRequest');

    console.log('SEND! message');
    request.send(params);

    name_input.value='';
    phone_input.value='';
    email_input.value='';
    text_message_input.value='';
    success_pop_show ('message')
}

function ajaxGet_for_call_btn (params){
    var call_phone_input=document.getElementById('call_phone');

    var request = new XMLHttpRequest();


    request.open('GET', '/recall'+'?'+params, false);

    request.onreadystatechange=function() {
        if (request.readyState == 4 && request.status == 200) {
            console.log('Вернулся ответ! recall');
            call_phone_input.value='';
            success_pop_show ('recall')
        }
    }

    request.setRequestHeader('X-REQUESTED-WITH', 'XMLHttpRequest');

    console.log('SEND! recall');
    request.send(null);
}


var pop_up_exit_id=document.getElementById('pop_up_exit_id');

var success_pop_off=function success_pop_off(event){
    pop_up_wrap_id.style.display='none';
    return false;

}

function popup_content(str1, str2) {
    var pop_up_content_elem=document.getElementsByClassName('pop_up_content')[0];
    var p1=pop_up_content_elem.getElementsByTagName('p')[0];
    var p2=pop_up_content_elem.getElementsByTagName('p')[1];
    p1.textContent=str1;
    p2.textContent=str2;
}

function success_pop_show (from_who){
    var pop_up_wrap_id=document.getElementById('pop_up_wrap_id');
    pop_up_wrap_id.style.display='block';

    if (from_who=='recall') {
        var str1='Заказ на обратный звонок принят!';
        var str2='Мы свяжемся с вами в ближайшее время.';
    }
    if (from_who=='message') {
        var str1='Ваша заявка успешно отправлена!';
        var str2='Мы свяжемся с вами в ближайшее время.';
    }
    if (from_who=='call btn validator') {
        var str1='Извините  =((';
        var str2='В данное время операторы недоступны';
    }
    popup_content(str1,str2)
}


message_btn.addEventListener("click", message_btn_var,false);
call_btn.addEventListener("click", call_btn_var,false);
pop_up_exit_id.addEventListener("click", success_pop_off, false);






























































