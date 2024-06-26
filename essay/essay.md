# Introduction

Literary historians of the United States broadly agree that, at some point during the nineteenth century, New York City overtakes Boston as the literary capital of the US. What Pascale Casanova argues Paris is for world literature, New York becomes for US literature specifically, and, eventually, Anglophone literatures more generally.[@casanovaWorldRepublicLetters2004]

Data recently released by the Library of Congress (LC) allows us to assess this historical claim in new ways, but not in the format in which it was originally released. By converting this data to a form useful for computational literary studies, I have evaluated this geographic shift, and made it possible for other scholars of nineteenth century US literatures to use the same data for a wide range of purposes. Perhaps more importantly, the code that extracted the data used to answer this nineteenth century question can be used to get any fields of interest from any set of the 11 million book catalog records that the LC has made public.

Nancy Glazener argues that the *Atlantic* magazine "had greater authority over American literature than any other institution did" in the latter half of the nineteenth century.^[@glazenerReadingRealismHistory1997, 5. See also @glazenerLiteratureMakingHistory2016.] Because of this, the shifting center of US literary culture from Boston to New York City is sometimes personified in *Atlantic* editor William Dean Howells. Howells moved from Ohio to Boston to make his literary mark, and then moved from Boston to New York in the 1880s.^[See, e.g., @bentleyLiteraryFormsMass2005a, 250. This symbolically important move cannot be pinned to a single year since, between 1886 and 1891, Howells moves back and forth between Boston and New York several times. @goodmanWilliamDeanHowells2005, xxiv, 279.]

Yet the material infrastructures of literary culture involved in such a shift---the means of production, distribution, and the skilled workers---could not possibly move as easily as Howells's prestige. While *The History of the Book in America* has already covered many details of these processes, it does not cover the changing imprint geographies of US publishing in general and US literary publishing in particular, in part because this data was neither publicly available nor in a computationally tractable form.[@casperIndustrialBook184018802007; @kaestlePrintMotionExpansion2009]

## LC MDS books data

For the first time in 2015 and most recently in 2020, the Library of Congress (LC) released its MARC Distribution Services (MDS) books dataset to the public, which contains more than 11 million book records.^[@BooksAllMDSConnect2020. Thanks to Jaime Mears specifically and LC Labs generally for informing me about this dataset, as well as directing me to past work using this data by Matt Miller and Jer Thorp.] Although these records cannot be said to list every relevant book, it nevertheless remains the largest such catalog to which there is public access.^[OCLC's WorldCat might be more comprehensive, but access is limited.]

[Figure 1](https://lccn.loc.gov/07017953) shows how one very famous record among the 11 million appears on the web.

![A screenshot of the LC catalog record for *Moby-Dick* (1851).](../moby.png){width=10cm}

And here is some of the underlying XML that creates that view of the record, and which exemplifies how all of the records are formatted:

```xml
<datafield ind1="1" ind2="0" tag="245">
    <subfield code="a">Moby-Dick :</subfield>
    <subfield code="b">or, The whale /</subfield>
    <subfield code="c">by Herman Melville ...</subfield>
  </datafield>
  <datafield ind1=" " ind2=" " tag="260">
    <subfield code="a">New York :</subfield>
    <subfield code="b">Harper &amp; Brothers ;</subfield>
    <subfield code="a">London :</subfield>
    <subfield code="b">Richard Bentley,</subfield>
    <subfield code="c">1851.</subfield>
  </datafield>
```

All of these records were created by librarians to describe "monographs written in nearly all the world's languages and published anywhere" including "Cataloging in Publication (CIP) records and minimal level cataloging records."[@BooksAllDatabase2024] My contribution is extracting, cleaning, and analyzing the data that librarians created in a way that is immediately useful for scholars of US literature in the long nineteenth century, provides both a working model and code for those in any other field who wish to work with any of the millions of LC MARC records I do not consider here, and publicizes the uses of this resource to address questions of literary history.

## Measuring imprint geographies

Americanists will perhaps be excessively familiar with the "PS" subclass of the LC's Language and Literature classification ("P"), which I use to study the changing imprint geographies of US literature over the long nineteenth century.[@LibraryCongressClassification2024] Generally, I check every classification value of every record to see if any of its classifications are part of the "PS" subclass. I then extract selected fields from the relevant records. Finally, I apply two cleaning steps to the year and place of publication to make them computationally tractable for my purposes. Readers interested in the details should consult [the repository](https://github.com/erikfredner/c19dc), which includes code to reproduce these results locally, and which can be trivially modified to extract records and fields in which they may be interested.[@frednerGettingNineteenthCentury2024]

Given the received narrative from US literary histories, I expected to see New York's publishing dominance rise consistently over the century, reaching a more or less unchallenged position after Reconstruction begins in 1865. But the data only partially support that narrative.

![Five-year rolling average of the total number of LC American literature books, 1745-1945.](../lc_ps_city.png)

The graph shows the absolute growth in the amount of annual publishing in American literature. Note that this represents cataloged publications, not sales or any other measure of readership beyond cataloging librarians' judgment. It is quite likely that books printed in New York sold better than books printed in, say, Indianapolis, which is the eighth most frequent place of publication in this period. But this data cannot tell us much about that disparity.

![Five-year rolling average of the proportion of LC American literature books, 1800-1945.](../lc_city_year_normed.png)

However, the absolute growth in publication makes it difficult to see the changing geographies of US imprints. Measuring proportional change suggests that serious contestation among Boston, Philadelphia, and New York to be the publishing capital of US literature is over as early as the 1840s, not in the post-Civil War period as is often assumed. More important than revising a timeline, however, is this: The data suggest that it is never the case that more than half of US literature has a New York imprint. Measured in catalog records, most of US literary publishing happens elsewhere. Relatedly, the big surprise of these charts is the size of "Other," which represents every place of publication not named in the legend. Up to the 1850s, "Other" was far larger than any single city, and, as Boston and Philadelphia decline, it keeps pace with (and occasionally exceeds) New York. New York is the most important place, but it is far from the only place.

There is much more to be said about these charts elsewhere. For now, suffice it to say that this example shows how one can use the transformed MDS Connect data to study questions of historical and critical interest for nineteenth century literatures. Other possible applications of the data---modeling republications, the distribution of unique authors, mining the text of the titles, the distribution of publishers, etc.---abound within the data published with this essay. Other LC record fields not included like subject headings (e.g., "Ahab, Captain (Fictitious character)--Fiction. Mentally ill--Fiction.") could be rich. By means of small adjustments the code in the repository, anyone interested in other geographies, other periods, or other fields can extract data from any subset of the LC's 11 million public records.

## Works Cited
