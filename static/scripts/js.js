   function check_password( )
      {
        if (document.getElementById('password').value ==123 )
          {
            window.open('html_js.html','_blank');
          }
        else
          {
            alert("Password is Rong!");
          }
      }

function click() {
  if (document.getElementById("password").value == "123") {
    console.log("Login is True...");
  } else {
    console.log("Password is error");
  }
}

  function go_home( )
      {
            window.open('/main','_blank');
      }


function search_field( )
      {
        if (document.getElementById('search').value  )
            {
                alert("Search is Done!");
            }
        else
            {
                alert("Enter data in field saerch !");
            }
      }


      
function focusNextField(event, nextFieldId) {
  if (event.key === "Enter") {
    event.preventDefault(); // Prevent form submission
    document.getElementById(nextFieldId).focus();
  }
}
