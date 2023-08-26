  
  let count = 0;
  function closenav(){
          const SideNav = document.getElementById("sideNav");
          const SideNavList = document.getElementById("sidenavlist");
          const mainContent = document.getElementById("maincontent");
          const spans = document.querySelectorAll('.side-nav-list li span'); // Select all <span> elements within list items
          const closenav = document.getElementById("closenav");
          
          number = count++;
  
          if (number%2 == 0){
              SideNav.classList.add("active");
              SideNavList.classList.add("active");
              mainContent.classList.add("active");
              // closenav.style.display = "none";
              closenav.innerHTML = '<i class="fas fa-angle-right"></i>'; // Change icon to close
              
              spans.forEach(span => {
                span.style.display = 'none';
              });
          

              document.documentElement.style.setProperty('--side_nav_width', '5rem');

              console.log(1);
          }
          else{
            SideNav.classList.remove("active");
            SideNavList.classList.remove("active");
            mainContent.classList.remove("active");
            const spans = document.querySelectorAll('.side-nav-list li span'); // Select all <span> elements within list items
            
            closenav.innerHTML = '<i class="fas fa-bars" ></i>'; 
            
            spans.forEach(span => {
              span.style.display = 'inline';
            });
        
           
            document.documentElement.style.setProperty('--side_nav_width', '260px');
            console.log(2);
          }

  }


  function toggleActive(clickedLink) {
    const links = document.querySelectorAll('.side-nav-list li a'); // Select all links
  
    links.forEach(link => {
      if (link === clickedLink) {
        link.classList.toggle('active'); // Toggle "active" class on clicked link
      } else {
        link.classList.remove('active'); // Remove "active" class from other links
      }
    });
  }
  