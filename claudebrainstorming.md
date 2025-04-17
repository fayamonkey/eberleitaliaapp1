Goal: Our goal is to create an app that automates a workflow that is right now done manually by a human:
The Eberle Germany ERP system produces an “Open Order List” excel file and sends it to Eberle Italia.On this list, we see all open orders at that time, referring to an “Artikelnummer”. This Artikelnummer is something specific to Eberle Germany. Eberle Italia uses another kind of ERP system and they use different kinds of specific Artikelnummern. At Eberle Italia, an employee now looks at the Open Order List sent by Eberle Germany and then produces a “Top-50” excel list from the Eberle Italia ERP System. This Top-50 list contains all the high value material and customers that have high priority for Eberle Italia. The Eberle Italia employee now compares those two files in this way: He starts from the first line in the top-50 file, looking up the codice in Row A: in our example case RM4210090#1801
Not the employee wants to know if this is also on the excel file sent by Eberle Germany. But the problem is that Eberle Germany uses a different codice for this material. For example, at Eberle Germany the same material is listed as 758967000. And it is also listed as 758897000. And many other numbers. That is because Eberle Germany is splitting up much more, while Eberle Italia is condensing. They have got one codice / Artikelnummer, which relates to multiple Artikelnummern in germany.
To make this easier, the employee has got a third excel file, a “translator-file”, which shows him RM4210090#1801 relates to which Artikelnummern bei Eberle. But it’s a bit more tricky than that: Inside of the Translator-file, we see the codice as RM4210090. Everything behind the # has been cut off. So the employee looks into the Top-50 file to extract RM4210090#1801, and then he looks into the Translator-file and searches for all lines with RM4210090. Since there can be multiple Artikelnummern for each codice, the employee now looks through the complete translator-file to find all corresponding Artikelnummern.
With this list of Artikelnummern, the employee now opens up the Open Order List from Eberle Germany, and he searches for every Artikelnummer and if it’s to be found inside of the list. If the Artikelnummer appears in here, we have a match! This complete line gets highlighted in red. Then the employee continues until he checked for all Artikelnummern belonging to RM4210090#1801.
Now the cycle begins anew: The employee starts over with the second codice from the Top-50 list, first finding the Artikelnummern it contains, and then comparing it to the Open Order List, in the way described above detailed.

I want to create an app that automates this process, so the user uploads the three files:

Open Order List (Eberle Germany)
Translation File
Top-50 (Eberle Italia)

And then the user can start the process, and everything happens automatically then. And the result is:

The Open Order List Excel file for download, with highlighted (in red) lines that contain the Artikelnummern we were matching with

An Excel file with the summary of the process and findings: The Eberle Italia codice in row A, the cut off codice in row B, the corresponding Artikelnummern in the next rows

Here is a detailed description of each excel file and what we need out of it:

Top-50 (contains 150 lines, can vary):

We need the codice from row A


Translator-File:

The chunked codices (just the part before the #) are in row D
The corresponding Artikelnummer is in row Q

Mind that in this file, we have got the same codice in row D multiple times, each time with other corresponding Artikelnummern in row Q


Open Order List:

In this file, we only need to look into row C to find the correlating Artikelnummern. If we find a match here, this line gets highlighted in red.


Additional information transportation:
There is three additional columns we need to extract information from in the Top-50 excel file: 
Columns D, G and K. D is Lagerbestand, G is Kundenauftraege, K is Monatlicher Verbrauch. Those are the three values that we need to extract and attach in this way inside a new file:

First, we look at our file that contains the translation:
Column A for RM4210090#1801, Column B for RM4210090 (the chunked file), Column C for Artikelnumbers it refers to, so Column C contains a lot of those 7758928000 numbers.

We need to split up this list into a new one that connects: RM4210090#1801, RM4210090, 7758928000, Lagerbestand value, Kundenauftraege Value, Monatlicher Verbrauch Value

And then, if RM4210090#1801 contains multiple Artikelnummern, we need to do the same for every Artikelnummer:
RM4210090#1801, RM4210090, 7708123000, Lagerbestand value, Kundenauftraege Value, Monatlicher Verbrauch Value

And so on. This way, we have a connection between all of those values. And when the final open order list gets created, the matching Artikelnummer lines will be found and highlighted /marked in red. And also for each match, we see the corresponding values of columns D, G and K from the top 50 list.

