document.getElementById("bbtn").addEventListener("click", function () { 
   
    alert(" Message sent !  Thank you For Your Comment");
});







function Wedding(firstName,lastName, phone,country, email,eventDetails,date,eventType, number,preferedVenues,price) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.phone = phone;
    this.country = country;
    this.email = email;
    this.eventDetails = eventDetails;
    
    this.date = date;
    this. eventType = eventType;
    this. number = number;
    this. preferedVenues = preferedVenues;
    this.price = price;
   
  }
  Wedding.prototype.fullBook = function() {
    return (
      this.firstName +
      " " +
      this.lastName +
      " " +
      this.phone +
      " " +
      this.country +
      " " +
      this.email +
      " " +
      this.eventDetails +
      " " + 
      this.date +
      " " + 
      this.eventType +
      " " + 
      this.number +
      " " + 
      this.preferedVenues +
      " " + 
      this.price
    );
  };
  $(document).ready(function() {
    $("#btn").click(function() {
       $("form#form").submit(function(event) {
           event.preventDefault();
  
      var fName = $("input#firstName").val();
      var lName = $("input#lastName").val();
      var phon = $("input#phone").val();
      var countr = $("input#country").val();
      var emai = $("input#email").val();
      var dFlex = $("input#flexible").val();
      var dat = $("input#date").val();
      var typ = $("select#type").val();
      var numbers = $("input#number").val();
      var preff = $("select#preffered").val();
     
      
    //   $("ul#we").append("<li><span class='contact'>" + newBook.fullBook() + "</span></li>");

    if(preff === "Arena Wedding Hall" && typ === "Reception"){
        prices = 2000000;
  }
  else if(preff === "Arena Wedding Hall" && typ === "Dowry")
  {
      prices = 1500000;
  }else if(preff === "Convention Wedding Hall" && typ === "Dowry")
  {
      prices = 1400000;
  }
  else if(preff === "Convention Wedding Hall" && typ === "Reception")
  {
      prices = 1800000;
  }
  else if(preff === "Heaven Garden Rebero" && typ === "Reception")
  {
      prices = 1000000;
  }
  else if(preff === "Heaven Garden Rebero" && typ === "Dowry")
  {
      prices = 800000;
  }
  else if(preff === "Serena Wedding Hall" && typ === "Dowry")
  {
      prices = 700000;
  }
  else if(preff === "Serena Wedding Hall" && typ === "Reception")
  {
      prices = 800000;
  }
  else if(preff === "Marriot Wedding Hall" && typ === "Dowry")
  {
      prices = 900000;
  }
  else if(preff === "Marriot Wedding Hall" && typ === "Reception")
  {
      prices = 1000000;
  }
  else if(preff === "Ituze Garden" && typ === "Dowry")
  {
      prices = 400000;
  }
  else if(preff === "Ituze Garden" && typ === "Reception")
  {
      prices = 600000;
  }
  else if(preff === "La palme wedding Hall" && typ === "Dowry")
  {
      prices = 500000;
  }
  else if(preff === "La palme wedding Hall" && typ === "Reception")
  {
      prices = 700000;
  }
  else if(preff === "Greenwich wedding Hall" && typ === "Dowry")
  {
      prices = 300000;
  }
  else if(preff === "Greenwich wedding Hall" && typ === "Reception")
  {
      prices = 550000;
  }
  else if(preff === "Hill View wedding Hall" && typ === "Dowry")
  {
      prices = 400000;
  }
  else if(preff === "Hill View wedding Hall" && typ === "Reception")
  {
      prices = 600000;
  }
  else{
      alert("Try again");
  }
  var prices;
      var newBook = new Wedding( fName,lName,phon,countr,emai,dFlex,dat,typ,numbers,preff,prices);
      console.log(newBook);

      $("#show-order").show();
    
        $(".firstName").text(newBook.firstName);
        $(".lastName").text(newBook.lastName);
        $(".phone").text(newBook.phone);
        $(".country").text(newBook.country);
        $(".email").text(newBook.email);
        $(".datef").text(newBook.eventDetails);
        $(".date").text(newBook.date);
        $(".type").text(newBook.eventType);
        $(".number").text(newBook.number);
        $(".preffered").text(newBook.preferedVenues);
        $(".price").text(newBook.price);


console.log(prices);
});
});
});
document.getElementById("btns").addEventListener("click", function () { 
   
    alert(" Message sent! Thank you for being our valued customer.    We are grateful for the pleasure of making your wedding more special .once again thank you !!");
});
