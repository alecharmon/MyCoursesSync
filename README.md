# ${1:McGill MyCourses Sync}
This is a functional beta for synching a local folder on your computer to your McGill mycourses classes it grew out of my hatred of worrying about wether or not I had everything that I needed downloaded from MyCourses. It was built using a combination of mechanize and selenium to scrape the links from your course pages and then download them locally. Ideally it would be something that you have in cron so that you would **NEVER NEED TO USE MYCOURSES EVER AGAIN**. 
## Installation
At the moment all you need is python, pip and firefox, all of the python dependencies are in requirements.txt

'''bash
pip install -r requirements.txt
'''

Also edit the config-example.yaml file so that it uses your credentials and the correct course. All courses should appear as they do in mycourses ie "Fall 2015" or "Winter 2013"


## Usage
just run 'python main.py' and you should be good to go.

Note:
Though it was built with firefox I would ideally like to get the project tested with PhantomJS for true headless syncing
TODO: Write usage instructions
## Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## License
The MIT License (MIT)

Copyright (c) 2015 Alec Harmon

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.