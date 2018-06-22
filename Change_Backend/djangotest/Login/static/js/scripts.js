
jQuery(document).ready(function() {
	
    /*
        Fullscreen background
    */
    $.backstretch("assets/img/backgrounds/1.jpg");
    
    /*
        Form validation
    */
    $('.login-form input[type="text"], .login-form input[type="password"], .login-form textarea').on('focus', function() {
    	$(this).removeClass('input-error');
    });
    
    $('.login-form').on('submit', function(e) {
    	
    	$(this).find('input[type="text"], input[type="password"], textarea').each(function(){
    		if( $(this).val() == "" ) {
    			e.preventDefault();
    			$(this).addClass('input-error');
    		}
    		else {
    			$(this).removeClass('input-error');
    		}
    	});
    	
    });
    
    
});

$('#facebook').on('click', function() {
  // Initialize with your OAuth.io app public key
  OAuth.initialize('HwAr2OtSxRgEEnO2-JnYjsuA3tc');
  // Use popup for oauth
  OAuth.popup('facebook').then(facebook => {
    console.log('facebook:',facebook);
    // Prompts 'welcome' message with User's email on successful login
    // #me() is a convenient method to retrieve user data without requiring you
    // to know which OAuth provider url to call
    facebook.me().then(data => {
      console.log('me data:', data);
      alert('Facebook says your email is:' + data.email + ".\nView browser 'Console Log' for more details");
    })
    // Retrieves user data from OAuth provider by using #get() and
    // OAuth provider url
    facebook.get('/v2.5/me?fields=name,first_name,last_name,email,gender,location,locale,work,languages,birthday,relationship_status,hometown,picture').then(data => {
      console.log('self data:', data);
    })
  });
})
