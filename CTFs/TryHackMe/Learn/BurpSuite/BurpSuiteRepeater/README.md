# Try Hack Me - [Burp Suite: Repeater](https://tryhackme.com/room/burpsuiterepeater)
##### Learn how to use Repeater to duplicate requests in Burp Suite

## Task 1 - Introduction Outline

Welcome to the Burp: Repeater room!

Having covered the basics of using Burp Suite, this room will dive into one of the more powerful aspects of the framework, namely: the Burp Suite Repeater module.

We will be covering how to use Repeater to manipulate and arbitrarily resend captured requests, as well as looking at some of the niftier options available in this awesome tool. Finally, we will encounter a series of examples, including a real-world, extra-mile exercise which we will use to consolidate the more theoretical aspects of the room.

If you have not used Burp Suite before and have not completed the Burp Basics room, you may wish to do so now before continuing, as this room builds on the foundations covered there.
```
Deploy the machine (and the AttackBox if you are not using your own attack VM), and let's get started!

Note: If you are not using the AttackBox and want to connect to this machine without the VPN, you can do so using this link once the machine has fully loaded and an IP address is displayed: https://LAB_WEB_URL.p.thmlabs.com.
> No answer needed
```

## Task 2 - Repeater What is Repeater?

Before we start using Repeater, it will help to have a good idea of what it does.

In short: Burp Suite Repeater allows us to craft and/or relay intercepted requests to a target at will. In layman's terms, it means we can take a request captured in the Proxy, edit it, and send the same request repeatedly as many times as we wish. Alternatively, we could craft requests by hand, much as we would from the CLI ( C ommand L ine I nterface), using a tool such as [cURL](https://curl.se/) to build and send requests.

This ability to edit and resend the same request multiple times makes Repeater ideal for any kind of manual poking around at an endpoint, providing us with a nice G raphical U ser I nterface (GUI) for writing the request payload and numerous views (including a rendering engine for a graphical view) of the response so that we can see the results of our handiwork in action.

The Repeater interface can be split into six main sections -- an annotated diagram can be found below the following bullet points:

1. At the very top left of the tab, we have a list of Repeater requests. We can have many different requests going through Repeater: each time we send a new request to Repeater, it will appear up here.
2. Directly underneath the request list, we have the controls for the current request. These allow us to send a request, cancel a hanging request, and go forwards/backwards in the request history.
3. Still on the left-hand side of the tab, but taking up most of the window, we have the request and response view. We edit the request in the Request view then press send. The response will show up in the Response view.
4. Above the request/response section, on the right-hand side, is a set of options allowing us to change the layout for the request and response views. By default, this is usually side-by-side (horizontal layout, as in the screenshot); however, we can also choose to put them above/below each other (vertical layout) or in separate tabs (combined view).
5. At the right-hand side of the window, we have the Inspector, which allows us to break requests apart to analyse and edit them in a slightly more intuitive way than with the raw editor. We will cover this in a later task.
6. Finally, above the Inspector we have our target. Quite simply, this is the IP address or domain to which we are sending requests. When we send requests to Repeater from other parts of Burp Suite, this will be filled in automatically.

![](images/631e09c2296fbc8d73ed38afa9705a50.png)

Don't worry if this doesn't make too much sense just now -- you will get plenty of chances to learn what it does first hand in the upcoming tasks!
```
Familiarise yourself with the Repeater interface.
> No answer needed
```

## Task 3 - Repeater Basic Usage

We know what the interface looks like now, but how do we put it to use?

Whilst we can craft requests by hand, it would be much more common to simply capture a request in the Proxy, then send that through to Repeater for editing/resending.

With a request captured in the proxy, we can send to repeater either by right-clicking on the request and choosing "Send to Repeater" or by pressing ```Ctrl + R```.

Switching back to Repeater, we can see that our request is now available:

![](images/ae762b56b7ecb30a0d861221d41502f5.png)

The target and Inspector elements are now also showing information; however, we do not yet have a response. When we click the "Send" button, the Response section quickly populates:

![](images/11da62185a73223355048c2fc04a1340.png)

If we want to change anything about the request, we can simply type in the Request window and press "Send" again; this will update the Response on the right. For example, changing the "Connection" header to ```open``` rather than ```close``` results in a response "Connection" header with a value of ```keep-alive```:

![](images/67d1462106edc86bd676315b3c0cba08.png)

We could then also use the history buttons to the right of the Send button to go forwards and backwards in our modification history.
```
Capture a request to http://MACHINE_IP in the Proxy and send it to Repeater.

Practice modifying and re-sending the request numerous times.
> No answer needed
```

## Task 4 - Repeater Views

Repeater offers us various ways to present the responses to our requests -- these range from hex output all the way up to a fully rendered version of the page.

We can see the available options by looking above the response box:

![](images/635ad62b0204b104bbd58489716eccde.png)

We have four display options here:
1. Pretty: This is the default option. It takes the raw response and attempts to beautify it slightly, making it easier to read.
2. Raw: The pure, un-beautified response from the server.
3. Hex: This view takes the raw response and gives us a byte view of it -- especially useful if the response is a binary file.
4. Render: The render view renders the page as it would appear in your browser. Whilst not hugely useful given that we would usually be interested in the source code when using Repeater, this is still a neat trick.

In most instances, the "Pretty" option is perfectly adequate; however, it is still well worth knowing how to use the other three options.

Just to the right of the view buttons is the "Show non-printable characters" button (```\n```). This button allows us to display characters that usually wouldn't show up in the Pretty or Raw views. For example, every line in the response will end with the characters ```\r\n``` -- these signify a carriage return followed by a newline and are part of how HTTP headers are interpreted.

Whilst not required for most tasks, this option can still come in handy.
```
Experiment with the available view options.
> No answer needed
```

```
Which view option displays the response in the same format as your browser would?
> Render
```

## Task 5 - Repeater Inspector

In many ways, Inspector is entirely supplementary to the request and response fields of the Repeater window. If you understand how to read and edit HTTP requests, then you may find that you rarely use Inspector at all.

That said, it is a superb way to get a prettified breakdown of the requests and responses, as well as for experimenting to see how changes made using the higher-level Inspector affect the equivalent raw versions.

Inspector can be used in the Proxy as well as Repeater. In both cases, it appears over at the very right hand side of the window and gives us a list of the components in the request and response:

![](images/c365f42b324b823dfc928c28f3c41214.png)

Of these, the request sections can nearly always be altered, allowing us to add, edit, and delete items. For example, in the Request Attributes section, we can edit the parts of the request that deal with location, method and protocol; e.g. changing the resource we are looking to retrieve, altering the request from GET to another HTTP method, or switching protocol from HTTP/1 to HTTP/2:

![](images/4f3a0f3714ceebbd6016e077369b48e8.png)

The other sections available for viewing and/or editing are:

* Query Parameters, which refer to data being sent to the server in the URL. For example, in a GET request to ```https://admin.tryhackme.com/?redirect=false```, there is a query parameter called "redirect" with a value of "false".
* Body Parameters, which do the same thing as Query Parameters, but for POST requests. Anything that we send as data in a POST request will show up in this section, once again allowing us to modify the parameters before re-sending.
* Request Cookies contain, as you may expect, a modifiable list of the cookies which are being sent with each request.
* Request Headers allow us to view, access, and modify (including outright adding or removing) any of the headers being sent with our requests. Editing these can be very useful when attempting to see how a webserver will respond to unexpected headers.
* Response Headers show us the headers that the server sent back in response to our request. These cannot be edited (as we can't control what headers the server returns to us!). Note that this section will only show up after we have sent the request and received a response.

These components can all be found as text within the request and response sections; however, it can be nice to see them in the tabular format offered by Inspector. It is well worth adding, removing, and editing headers in Inspector to get a feel for how the raw version changes as you do so.
```
Get comfortable with Inspector and practice adding/removing items from the various request sections.
> No answer needed
```

## Task 6 - Practical Example

Repeater is best suited for the kind of task where we need to send the same request numerous times, usually with small changes in between requests. For example, we may wish to manually test for an SQL Injection vulnerability (which we will do in an upcoming task), attempt to bypass a web application firewall filter, or simply add or change parameters in a form submission.

For now, let's start with an extremely simple example: using Repeater to alter the headers of a request we send to a target.
```
Capture a request to http://MACHINE_IP/ in the Proxy and send it to Repeater.
> No answer needed
```

```
Send the request once from Repeater -- you should see the HTML source code for the page you requested in the response tab.Try viewing this in one of the other view options (e.g. Rendered).
> No answer needed
```

```
Using Inspector (or manually, if you prefer), add a header called FlagAuthorised and set it to have a value of True. e.g.:


            Headers with FlagAuthorised Added
        
GET / HTTP/1.1
Host: MACHINE_IP
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
FlagAuthorised: True



Send the request. What is the flag you receive?
> THM{Yzg2MWI2ZDhlYzdlNGFiZTUzZTIzMzVi}
```

## Task 7 - Practical Challenge

In the previous task, we used Repeater to add a header and send a request; this should serve as an example for using Repeater -- now it's time for a very simple challenge!

With your proxy deactivated, head over to ```http://MACHINE_IP/products/``` and try clicking on some of the "See More" links.

Do you notice that it redirects you to a numeric endpoint (e.g. ```/products/3```) when you click for more details?

This endpoint needs to be validated to ensure that the number you try to navigate to exists and is a valid integer; however, what happens if it is not adequately validated?
```
Capture a request to one of the numeric products endpoints in the Proxy, then forward it to Repeater.
> No answer needed
```

```
See if you can get the server to error out with a "500 Internal Server Error" code by changing the number at the end of the request to extreme inputs.

What is the flag you receive when you cause a 500 error in the endpoint?
> THM{N2MzMzFhMTA1MmZiYjA2YWQ4M2ZmMzhl}
```

## Task 8 - Extra Mile SQLi with Repeater

This task contains an extra-mile challenge, which means that it is a slightly harder, real-world application for Burp Repeater. If you feel comfortable performing a manual SQL Injection by yourself, you may skip to the last question and try this as a blind challenge; otherwise a guide will be given below.

Before we start on this challenge: if you don't already know the principles of SQLi, then it would be well worth your time checking out the room on the topic ; however, full steps will be provided, so you do not need in-depth knowledge of the principles behind SQL Injection to complete this task.

The brief is as follows:

There is a Union SQL Injection vulnerability in the ID parameter of the ```/about/ID``` endpoint. Find this vulnerability and execute an attack to retrieve the notes about the CEO stored in the database.
```
We know that there is a vulnerability, and we know where it is. Now we just need to exploit it!Let's start by capturing a request to http://MACHINE_IP/about/2 in the Burp Proxy. Once you have captured the request, send it to Repeater with Ctrl + R or by right-clicking and choosing "Send to Repeater".
> No answer needed
```

```
Now that we have our request primed, let's confirm that a vulnerability exists. Adding a single apostrophe (') is usually enough to cause the server to error when a simple SQLi is present, so, either using Inspector or by editing the request path manually, add an apostrophe after the "2" at the end of the path and send the request:


            Response Headers from the Server
        
GET /about/2' HTTP/1.1
Host: MACHINE_IP
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1

        
You should see that the server responds with a "500 Internal Server Error", indicating that we successfully broke the query:


            Response Headers from the Server
        
HTTP/1.1 500 INTERNAL SERVER ERROR 

> No answer needed
```


If we look through the body of the server's response, we see something very interesting at around line 40. The server is telling us the query we tried to execute:

```html
            Overly verbose error message showing the query

<h2>
    <code>Invalid statement: 
        <code>SELECT firstName, lastName, pfpLink, role, bio FROM people WHERE id = 2'</code>
    </code>
</h2>
```

This is an extremely useful error message which the server should absolutely not be sending us, but the fact that we have it makes our job significantly more straightforward.

The message tells us a couple of things that will be invaluable when exploiting this vulnerability:
* The database table we are selecting from is called people.
* The query is selecting five columns from the table: ```firstName```, ```lastName```, ```pfpLink```, ```role```, and ```bio```. We can guess where these fit into the page, which will be helpful for when we choose where to place our responses.
```
With this information, we can skip over the query column number and table name enumeration steps.
> No answer needed
```

Although we have managed to cut out a lot of the enumeration required here, we still need to find the name of our target column.

As we know the table name and the number of rows, we can use a union query to select the column names for the ```people``` table from the ```columns``` table in the ```information_schema``` default database.

A simple query for this is as follows:
```
/about/0 UNION ALL SELECT column_name,null,null,null,null FROM information_schema.columns WHERE table_name="people"
```
This creates a union query and selects our target then four null columns (to avoid the query erroring out). Notice that we also changed the ID that we are selecting from ```2``` to ```0```. By setting the ID to an invalid number, we�ensure that we don't retrieve anything with the original (legitimate) query; this means that the first row returned from the database will be our desired response from the injected query.

Looking through the returned response, we can see that the first column name (id) has been inserted into the page title:

```html
            The "id" column name in the title of the response
        
HTTP/1.1 200 OK
Server: nginx/1.18.0 (Ubuntu)
Date: Mon, 16 Aug 2021 22:12:36 GMT
Content-Type: text/html; charset=utf-8
Connection: close
Front-End-Https: on
Content-Length: 3360


<!DOCTYPE html>
<html lang=en>
    <head>
        <title>
            About | id None
        </title>
-----
```
```
> No answer needed
```

We have successfully pulled the first column name out of the database, but we now have a problem. The page is only displaying the first matching item -- we need to see all of the matching items.Fortunately, we can use our SQLi to group the results. We can still only retrieve one result at a time, but by using the group_concat()  function, we can amalgamate all of the column names into a single output:
```
/about/0 UNION ALL SELECT group_concat(column_name),null,null,null,null FROM information_schema.columns WHERE table_name="people"
```

This process is shown in below:

![](https://assets.muirlandoracle.co.uk/thm/modules/burp/94629aaae1f0.png)

```
> No answer needed
```

We have successfully identified eight columns in this table: ```id```, ```firstName```, ```lastName```, ```pfpLink```, ```role```, ```shortRole```, ```bi```o, and ```notes```.

Considering our task, it seems a safe bet that our target column is ```notes```.

Finally, we are ready to take the flag from this database -- we have all of the information that we need:
* The name of the table: ```people```.
* The name of the target column: ```notes```.
* The ID of the CEO is ```1```; this can be found simply by clicking on Jameson Wolfe's profile on the /about/ page and checking the ID in the URL.
 
Let's craft a query to extract this flag:
```
0 UNION ALL SELECT notes,null,null,null,null FROM people WHERE id = 1
```

Hey presto, we have a flag!

![](https://assets.muirlandoracle.co.uk/thm/modules/burp/1ec697198c99.png)

```
> No answer needed
```

```
Exploit the union SQL injection vulnerability in the site.

What is the flag?
> THM{ZGE3OTUyZGMyMzkwNjJmZjg3Mzk1NjJh}
```

## Task 9 - Conclusion Room Conclusion

We have now completed the Burp Suite Repeater room.

You should hopefully now understand how to use Repeater to edit, manipulate, and resend a request, as well as having an idea about the (many) practical applications for this.

The next room in the module will go on to look at the Burp Suite Intruder tool.
```
I can use Burp Suite Repeater!
> No answer needed
```

## Additional Resources