$(document).ready(function{
  $("#submit").click(function{
    var first = $("#firstName").val();
    var last = $("#lastName").val();
    var username = $("#username").val();
    var email = $("#inputEmail").val();
    var pwd = $("#inputPassword").val();
    var vpwd = $("#verifyPassword").val();

    if(first == '' || last == '' || username == '' || email == '' || pwd == '' || vpwd == ''){
      alert("All fields must be filled.");
    }
    else if(!pwd.match(vpwd)){
      alert("Passwords do not match.");
    }
    else if(pwd.length < 8){
      alert("Password must be at least 8 characters in length.");
    }
  });
});
