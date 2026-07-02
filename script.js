async function pay(){

if(!document.getElementById("agree").checked){
alert("कृपया नियम और शर्तें स्वीकार करें।");
return;
}

if(!document.getElementById("uname").value||!document.getElementById("uphone").value){
alert("कृपया नाम और मोबाइल नंबर भरें।");
return;
}

const order=await fetch("/create-order",{
method:"POST"
});

const data=await order.json();

var options={
key:"rzp_live_T8XptW4xmDFEIt",

amount:data.amount,

currency:"INR",

name:"Premium Movies",

order_id:data.id,

prefill:{
name:document.getElementById("uname").value,
email:document.getElementById("uemail").value,
contact:document.getElementById("uphone").value
},

handler:function(res){

fetch("/verify",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify(res)

})

.then(r=>r.json())

.then(d=>{

document.getElementById("result").innerHTML=

`<a href="${d.link}" target="_blank">
<button>Join Telegram</button>
</a>`;

});

}

};

new Razorpay(options).open();

}
