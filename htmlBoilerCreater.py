

fileIndexHTML = open('index.html','w')
fileStyleCSS = open('style.css','w')
fileScriptJS = open('script.js','w')

defaultHTML = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <script src="script.js" defer></script>
    
</head>
<body>
    
</body>
</html> '''

defaultCSS = '''*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
'''

defaultJS = '''"use strict"'''

# Adding boiler plate code into the files 


fileIndexHTML.write(defaultHTML)
fileIndexHTML.close()

fileStyleCSS.write(defaultCSS)
fileStyleCSS.close()

fileScriptJS.write(defaultJS)
fileScriptJS.close()
