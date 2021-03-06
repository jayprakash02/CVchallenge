<h1>DjangoAPI:Converting PDF text into JSON for ML Processing</h1>
    <p>You cannot go straight from raw text to fitting a machine learning or deep learning model.</p>
    <p>You must clean your text first, which means splitting it into words and handling punctuation and case.</p>        
    <p>In fact, there is a whole suite of text preparation methods that you may need to use, and the choice of methods really depends on your natural language processing task.</p>
    <h4>Text Cleaning Is Task Specific</h4>
    <p>After actually getting a hold of your text data, the first step in cleaning up text data is to have a strong idea about what you’re trying to achieve, and in that context review your text to see what exactly might help.</p> 
    <p><strong>Here’s what I see:</strong></p>
    <ul>
    <li>It’s plain text so there is no markup to parse (yay!).</li>
    <li>The translation of the original German uses UK English (e.g. “travelling“).</li>
    <li>The lines are artificially wrapped with new lines at about 70 characters (meh).</li>
    <li>There’s punctuation like commas, apostrophes, quotes, question marks, and more.</li>
    <li>There’s hyphenated descriptions like “armour-like”.</li>
    <li>There’s a lot of use of the em dash (“-“) to continue sentences (maybe replace with commas?).</li>
    <li>There are names (e.g. “Mr. Samsa“)</li>
    <li>There does not appear to be numbers that require handling (e.g. 1999)</li>
    <li>There are section markers (e.g. “II” and “III”), and we have removed the first “I”.</li>
    </ul>
    <h4>INSTALLATION</h4>
    <p>STEP 1:<strong><code>pip install -r requirements.txt</code></strong></p>
    <p>After installation, you will need to install the data used with the library, including a great set of documents
        that you can use later for testing other tools in NLTK.</p>
    <p>STEP 2:<br><strong><code> >>import nltk </br> >>nltk.download()</code></strong></p>
    <p>Now time for Setting Up Django</p>
    <p>STEP 3:
        Migrations<br><strong><code>python manage.py makemigrations</code></strong><br><strong><code>python manage.py migrate</code></strong>
    </p>
    <p>STEP 4: Creating SuperUser<br><strong><code>python manage.py createsuperuser</code></strong><br></p>
    <p>Fill the feilds and create superuser</p>
    <p>STEP 5: All set Create Server<br><strong><code>python manage.py runserver</code></strong><br>Open the localHost
    </p>
<h4>Let’s demonstrate this with a small pipeline of text preparation including:</h4>
<ol>
    <li>Load the raw text.</li>
    <li>Split into tokens.</li>
    <li>Convert to lowercase.</li>
    <li>Remove punctuation from each token using <b><i>NLTK</i></b> tokkens.</li>
    <li>Filter out remaining tokens that are not alphabetic using <i>NLTK</i> tokkens.</li>
    <li>Filter out tokens that are stop words using <i>NLTK</i> tokkens.</li>
    <li>Filter out stem words using <i>NLTK</i> tokkens.</li>
    <li>Convert the stem list into string and put in the file.</li>    
</ol>
<h4>Let’s demonstrate the Conversion pipeline</h4>
<ol>
    <li>The input PDF will be readed using <b><i>PyPDF2</i></b></li>
    <li>The <b>PyPDF2</b> will  read the PDF and store <b>text</b> into a string</li>
    <li>The string will be goes through the conversion pipeline</li>
    <li>The converted string will store into Model and replace the existing PDF with  <b>.csv</b> file.</li>
</ol>
<h4>Let’s demonstrate the API pipeline</h4>
<ol>
    <li>Input the PDF file in the API.</li>
    <li>The API will extract all the <b>text</b> and save into the <b>.csv</b> file.</li>
    <li>Then the output will give the <b>csv</b> file</li>
    <li>In the Second API input the number of words you want to generate</li>
    <li>This words are the most common words in the all csv</li>
    <li>And outpt will b in <b>.json</b> format</li>
</ol>
<a href="https://raw.githubusercontent.com/jayprakash02/CVchallenge/master/linkedinprofile.zip">Click here</a><p>To Download 50 Linkedin Profile(PDF) for Practical.</p>
