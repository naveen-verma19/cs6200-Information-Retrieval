import time
from random import randint
from fibheap import *


# heap1 = makefheap()
# h = []
# n = 100
# r=100
b=fheappush(heap1,0.01)
# hasg={}
# hasg["u"]=a
# k=hasg["u"]
# k.key=-1
# c=heap1.extract_min()
# print(c.key)
from crawler import get_relevance_factor, get_relevance_count

s="""The AP1000 is a nuclear power plant designed and sold by Westinghouse Electric Company. The plant is a pressurized water reactor with improved use of passive nuclear safety and many design features intended to lower its capital cost and improve its economics.

The design traces its history to the successful System 80 design, which was produced in various locations around the world. This initially led to the AP600 concept, with a smaller 600 to 700 MWe output, but this saw limited interest. In order to compete with other designs that were scaling up in size in order to improve capital costs, the design re-emerged as the AP1000 and found a number of design wins at this larger size.

Six AP1000s are currently in operation or under construction. Four are located at two sites in China, two at Sanmen Nuclear Power Station and two at Haiyang Nuclear Power Plant. Two are under construction at the Vogtle Electric Generating Plant in the US, while a further two at the Virgil C. Summer Nuclear Generating Station were cancelled in 2017. As of 2019, all four Chinese plants have completed construction and are at various stages of connecting to the grid. Construction at Vogtle has suffered numerous delays and Unit 3 is now expected to be completed in 2021. Cost overruns at Vogtle and the cancellation of Summer led to Westinghouse's bankruptcy in 2017.

The first AP1000 began operations in China at Sanmen, where Unit 1 became the first AP1000 to achieve criticality in June 2018,.[1] and was connected to the grid the next month. Further builds in China will be based on the modified CAP1400 design.


Contents
1	History
1.1	Previous work
1.2	AP1000
2	Design specifications
3	Design disputes
4	Chinese design extensions
5	Construction plans
5.1	China
5.2	United States
5.3	Bulgaria
5.4	United Kingdom
5.5	India
6	Operations
7	See also
8	References
9	External links
History
Previous work
	
This section needs additional citations for verification. (May 2019) (Learn how and when to remove this template message)
The AP1000 design traces its history to two previous designs, the AP600 and the System 80.

The System 80 design was created by Combustion Engineering and featured a two-loop cooling system with a single steam generator paired with two reactor coolant pumps in each loop that makes it simpler and less expensive than systems which pair a single reactor coolant pump with a steam generator in each of two, three, or four loops. Built to the extent of three reactors in the US and another four in South Korea, it was among the most successful Generation II+ designs. ABB Group bought Combustion Engineering in 1990 and introduced the System 80+, with a number of design changes and safety improvements. As part of a series of mergers, purchases and divestitures by ABB, in 2000 the design was purchased by Westinghouse Electric Company, who had itself been purchased in 1999 by British Nuclear Fuels Ltd (BNFL).

Through the 1990s, Westinghouse had been working on a new design known as the AP600 with a design power of about 600 MWe. This was part of the Department of Energy's Advanced Light Water Reactor program that worked on a series of Generation III reactor designs. In contrast to Generation II designs, the AP600 was much simpler, with a huge reduction in the total number of parts, and especially pumps. It was also passively safe, a key feature of Gen III designs.[2]

The AP600 was at the small end of the reactor scale. Smaller plants are periodically introduced because they can be used in a wider variety of markets where a larger reactor is simply too powerful. The downside of such designs is that the construction time, and thus cost, does not differ significantly to larger designs, so these smaller designs often have less attractive economics. The AP600 addressed this through modular construction and aimed to go from first concrete to fuel load in 36 months. In spite of these attractive features, Westinghouse had no sales of the AP600.[2]

With the purchase of the company by BNFL and its merger with ABB, a design combining the features of the System 80+ with the AP600 started as the AP1000. BNFL in turn sold Westinghouse Electric to Toshiba in 2005.

AP1000
In December 2005, the Nuclear Regulatory Commission (NRC) approved the final design certification for the AP1000.[3] This meant that prospective US builders could apply for a Combined Construction and Operating License before construction starts, the validity of which is conditional upon the plant being built as designed, and that each AP1000 should be identical. Its design is the first Generation III+ reactor to receive final design approval from the NRC.[4] In 2008 China started building four units of the AP1000's 2005-design.

In December 2011, the NRC approved construction of the first US plant to use the design.[5] On February 9, 2012 the NRC approved the construction of two new reactors.[6]

In 2016 and 2017 cost overruns constructing AP1000 plants in the U.S. caused Westinghouse's owner Toshiba to write down its investment in Westinghouse by "several billion" dollars.[7] On 14 February 2017 Toshiba delayed filing financial results, and Toshiba chairman Shigenori Shiga, formerly chairman of Westinghouse, resigned.[8][9][10] On March 24, 2017, Toshiba announced that Westinghouse Electric Company will file for Chapter 11 bankruptcy because of US$9 billion of losses from nuclear reactor construction projects, which may impact the future of the AP1000.[11] Westinghouse emerged from bankruptcy in August 2018.[12]

Date	Milestone
January 27, 2006	NRC issues the final design certification rule (DCR)
March 10, 2006	NRC issues revised FDA for Revision 15 of the Westinghouse design
May 26, 2007	Westinghouse applies to amend the DCR (Revision 16)
September 22, 2008	Westinghouse updated its application
October 14, 2008	Westinghouse provides a corrected set for Revision 17 of the design
December 1, 2010	Westinghouse submits Revision 18 of the design
June 13, 2011	Westinghouse submits Revision 19 of the design
December 30, 2011	NRC issues the final DC amendment final rule
Design specifications
The AP1000 is a pressurized water reactor[3] with two cooling loops, planned to produce a net power output of 1,117 MWe.[13] It is an evolutionary improvement on the AP600,[4] essentially a more powerful model with roughly the same footprint.[3]

A design objective was to be less expensive to build than other Generation III reactor designs, by both using existing technology, and needing less equipment than competing designs that have three or four cooling loops. The design decreases the number of components, including pipes, wires, and valves. Standardization and type-licensing should also help reduce the time and cost of construction. Because of its simplified design compared to a Westinghouse generation II PWR, the AP1000 has:[13]

50% fewer safety-related valves
35% fewer pumps
80% less safety-related piping
85% less control cable
45% less seismic building volume
The AP1000 design is considerably more compact in land usage than most existing PWRs, and uses under a fifth of the concrete and rebar reinforcing of older designs.[13] Probabilistic risk assessment was used in the design of the plants. This enabled minimization of risks, and calculation of the overall safety of the plant. According to the NRC, the plants will be orders of magnitude safer than those in the last study, NUREG-1150. The AP1000 has a maximum core damage frequency of 5.09 × 10−7 per plant per year.[14] Used fuel produced by the AP1000 can be stored indefinitely in water on the plant site.[15] Aged used fuel may also be stored in above-ground dry cask storage, in the same manner as the currently operating fleet of US power reactors.[13]

Power reactors of this general type continue to produce heat from radioactive decay products even after the main reaction is shut down, so it is necessary to remove this heat to avoid meltdown of the reactor core. In the AP1000, Westinghouse's Passive Core Cooling System uses a tank of water situated above the reactor. When the passive cooling system is activated, the water flows by gravity to the top of the reactor where it evaporates to remove heat. The system uses multiple explosively-operated and DC operated valves which must operate within the first 30 minutes. This is designed to happen even if the reactor operators take no action.[16] The electrical system required for initiating the passive systems doesn't rely on external or diesel power and the valves don't rely on hydraulic or compressed air systems.[3][17] The design is intended to passively remove heat for 72 hours, after which its gravity drain water tank must be topped up for as long as cooling is required.[13]

Revision 15 of the AP1000 design has an unusual containment structure which has received approval by the NRC, after a Safety Evaluation Report,[18] and a Design Certification Rule.[19] Revisions 17, 18, and 19 were also approved.[20]

Design disputes
In April 2010, some environmental organizations called on the NRC to investigate possible limitations in the AP1000 reactor design. These groups appealed to three federal agencies to suspend the licensing process because they believed containment in the new design is weaker than existing reactors.[21]

In April 2010, Arnold Gundersen, a nuclear engineer commissioned by several anti-nuclear groups, released a report which explored a hazard associated with the possible rusting through of the containment structure steel liner. In the AP1000 design, the liner and the concrete are separated, and if the steel rusts through, "there is no backup containment behind it" according to Gundersen.[22] If the dome rusted through the design would expel radioactive contaminants and the plant "could deliver a dose of radiation to the public that is 10 times higher than the N.R.C. limit" according to Gundersen. Vaughn Gilbert, a spokesman for Westinghouse, has disputed Gundersen's assessment, stating that the AP1000's steel containment vessel is three-and-a-half to five times thicker than the liners used in current designs, and that corrosion would be readily apparent during routine inspection.[22]

Edwin Lyman, a senior staff scientist at the Union of Concerned Scientists, has challenged specific cost-saving design choices made for both the AP1000 and ESBWR, another new design. Lyman is concerned about the strength of the steel containment vessel and the concrete shield building around the AP1000, claiming its containment vessel does not have sufficient safety margins.[23]

John Ma, a senior structural engineer at the NRC was quoted on his stance about the AP1000 nuclear reactor.[23]

In 2009, the NRC made a safety change related to the events of September 11, ruling that all plants be designed to withstand the direct hit from a plane. To meet the new requirement, Westinghouse encased the AP1000 buildings concrete walls in steel plates. Last year Ma, a member of the NRC since it was formed in 1974, filed the first "non-concurrence" dissent of his career after the NRC granted the design approval. In it Ma argues that some parts of the steel skin are so brittle that the "impact energy" from a plane strike or storm driven projectile could shatter the wall. A team of engineering experts hired by Westinghouse disagreed...[23]

In 2010, following Ma's initial concerns, the NRC questioned the durability of the AP1000 reactor's original shield building in the face of severe external events such as earthquakes, hurricanes, and airplane collisions. In response to these concerns Westinghouse prepared a modified design.[24] This modified design satisfied the NRC, with the exception of Ma, hence the "non-concurrence". In contrast to the NRC's decision, Ma believed that computer codes used to analyze the modified design were not precise enough and some of the materials used were too brittle.[25]

A US consultant engineer has also criticized the AP1000 containment design arguing that, in the case of a design-basis accident, it could release radiation; Westinghouse has denied the claim.[26] The NRC completed the overall design certification review for the amended AP1000 in September 2011.[27]

In May 2011, US government regulators found additional problems with the design of the shield building of the new reactors. The chairman of the Nuclear Regulatory Commission said that: computations submitted by Westinghouse about the building's design appeared to be wrong and "had led to more questions."; the company had not used a range of possible temperatures for calculating potential seismic stresses on the shield building in the event of, for example, an earthquake; and that the commission was asking Westinghouse not only to fix its calculations but also to explain why it submitted flawed information in the first place. Westinghouse said that the items the commission was asking for were not "safety significant".[28]

In November 2011, Arnold Gundersen published a further report on behalf of the AP1000 Oversight Group, which includes Friends of the Earth and Mothers against Tennessee River Radiation. The report highlighted six areas of major concern and unreviewed safety questions requiring immediate technical review by the NRC. The report concluded that certification of the AP1000 should be delayed until the original and current “unanswered safety questions” raised by the AP1000 Oversight Group are resolved.[29]

In 2012, Ellen Vancko, from the Union of Concerned Scientists, said that "the Westinghouse AP1000 has a weaker containment, less redundancy in safety systems, and fewer safety features than current reactors".[30] In response to Ms. Vancko's concerns, climate policies author and retired nuclear engineer Zvi J. Doron, replied that the AP1000's safety is enhanced by fewer active components, not compromised as Ms. Vancko suggests.[30] As in direct contrast to currently operating reactors, the AP1000 has been designed around the concept of passive nuclear safety. In October 2013, Li Yulun, a former vice-president of China National Nuclear Corporation (CNNC), raised concerns over the safety standards of the delayed AP1000 third-generation nuclear power plant being built in Sanmen, due to the constantly changing, and consequently untested, design. Citing a lack of operating history, he also questioned the manufacturer's assertion that the AP1000 reactor's "primary system canned motor pumps"[31] were "maintenance-free" over 60 years, the assumed life of the reactor and noted that the expansion from 600 to 1,000 megawatts has not yet been commercially proven.[32]

Chinese design extensions
In 2008 and 2009, Westinghouse made agreements to work with the Chinese State Nuclear Power Technology Corporation (SNPTC) and other institutes to develop a larger design, the CAP1400 of 1,400 MWe capacity, possibly followed by a 1,700 MWe design. China will own the intellectual property rights for these larger designs. Exporting the new larger units may be possible with Westinghouse's cooperation.[33][34]

In September 2014, the Chinese nuclear regulator approved the design safety analysis following a 17-month review.[35] In May 2015 the CAP1400 design passed an International Atomic Energy Agency's Generic Reactor Safety Review.[36]

In December 2009, a Chinese joint venture was set up to build an initial CAP1400 near the HTR-PM at Shidao Bay Nuclear Power Plant.[33][37] In 2015, site preparation started, and approval to progress was expected by the end of the year.[38][39] In March 2017, the first CAP1400 reactor pressure vessel passed pressure tests.[40]

In February 2019, the Shanghai Nuclear Engineering Research & Design Institute announced that it had begun the conceptual design process for the CAP1700.[41]

Construction plans
China

Sanmen Nuclear Power Plant, the world's first AP1000, was commissioned in 2018.
Four AP1000 reactors were constructed in China, at Sanmen Nuclear Power Plant in Zhejiang, and Haiyang Nuclear Power Plant in Shandong.[42] The Sanmen unit 1 and unit 2 AP1000s were connected to the grid on 2 July 2018 and 24 August 2018 respectively.[43] Haiyang 1 started commercial operation on October 22, 2018,[44] Haiyang 2 on January 9, 2019.[45]

In 2014, China First Heavy Industries manufactured the first domestically produced AP1000 reactor pressure vessel, for the second AP1000 unit of Sanmen Nuclear Power Station.[46]

The first four AP1000s to be built are to an earlier revision of the design without a strengthened containment structure to provide improved protection against an aircraft crash.[47] China had officially adopted the AP1000 as a standard for inland nuclear projects.[48] But following Westinghouse's bankruptcy in 2017, decided in 2019 to build the domestically designed Hualong One rather than the AP1000 at Zhangzhou.[49]

United States
Two reactors are being constructed at the Vogtle Electric Generating Plant In the state of Georgia (Units 3 & 4).[50]

In South Carolina, two units were being constructed at the Virgil C. Summer Nuclear Generating Station (Units 2 & 3).[51] The project was abandoned in July 2017, 4 years after it began, due to Westinghouse's recent bankruptcy, major cost overruns, significant delays, and other issues.[52] The project's primary shareholder (SCANA) initially favored a plan to abandon development of Unit 3, while completing Unit 2. The plan was dependent on approval of a minority shareholder (Santee Cooper). Santee Cooper's board voted to cease all construction resulting in termination of the entire project.

All four reactors were identical and the two projects ran in parallel, with the first two reactors (Vogtle 3 and Summer 2) planned to be commissioned in 2019 and the remaining two (Vogtle 4 and Summer 3) in 2020.[53][54] After Westinghouse filed for bankruptcy protection on March 29, 2017, the construction has stalled.

On April 9, 2008, Georgia Power Company reached a contract agreement with Westinghouse and Shaw for two AP1000 reactors to be built at Vogtle.[55] The contract represents the first agreement for new nuclear development since the Three Mile Island accident in 1979.[56] The license request for the Vogtle site is based on revision 18 of the AP1000 design.[57] On February 16, 2010, President Obama announced $8.33 billion in federal loan guarantees to construct the two AP1000 units at the Vogtle plant.[58] The cost of building the two reactors is expected to be $14 billion.[59]

Environmental groups opposed to the licensing of the two new AP1000 reactors to be built at Vogtle filed a new petition in April 2011 asking the Nuclear Regulatory Commission's commission to suspend the licensing process until more is known about the evolving Fukushima I nuclear accidents.[60] In February 2012, nine environmental groups filed a collective challenge to the certification of the Vogtle reactor design and in March they filed a challenge to the Vogtle license. In May 2013, the U.S. Court of Appeals ruled in favor of the Nuclear Regulatory Commission (NRC).

In February 2012, the US Nuclear Regulatory Commission approved the two proposed reactors at the Vogtle plant.[61]

For VC Summer, a delay of at least one year and extra costs of $1.2 billion were announced in October 2014, largely due to fabrication delays. Unit 2 was then expected to be substantially complete in late 2018 or early 2019, with unit 3 about a year later.[62]

In October 2013, US energy secretary Ernest Moniz announced that China was to supply components to the US nuclear power plants under construction as part of a bilateral co-operation agreement between the two countries. Since China's State Nuclear Power Technology Corporation (SNPTC) acquired Westinghouses's AP1000 technology in 2006, it has developed a manufacturing supply chain capable of supplying international power projects. Industry analysts have highlighted a number of problems facing China's expansion in the nuclear market including continued gaps in their supply chain, coupled with Western fears of political interference and Chinese inexperience in the economics of nuclear power.[63]

On July 31, 2017, after an extensive review into the costs of constructing Units 2 and 3, South Carolina Electric and Gas decided to stop construction of the reactors at VC Summer and will file a Petition for Approval of Abandonment with the Public Service Commission of South Carolina.[64]

Bulgaria
On November 22, 2013, the Bulgarian economy and energy minister Dragomir Stoynev announced during a visit to the United States, that Bulgaria wants to build an AP1000 nuclear reactor as the seventh unit of the Kozloduy Nuclear Power Plant.[65] On December 11, the Bulgarian government gave its approval to Bulgarian Energy Holding (BEH) to start talks with Toshiba and Westinghouse on the new unit. Toshiba will hold a 30% share of the new unit. As of December 2013, the overall costs of the unit were estimated to be about $8 billion.[66] On December 13, talks between BEH and Westinghouse started.[67] As of December 2013, Westinghouse planned to complete preparatory work in nine months for technical, financial and economic parameters of the new unit,[68] so that construction can begin in 2016. In 2013 the Austrian Environment Agency's report on the Bulgarian Ministry for the Environment's Environmental Impact Assessment (EIA) on the proposed 7th unit of the Kozloduy Nuclear Power Plant found a number of unsubstantiated claims and some serious failings in the Bulgarian EIA report.[69] On July 30, 2014 a shareholder agreement has been signed by Westinghouse Electric Company LLC and the state-owned Kozloduy NPP for the construction of the Kozloduy-7 nuclear reactor and reactor block, for an estimated total price of $5 billion.[70]

United Kingdom
In December 2013, Toshiba, through its Westinghouse subsidiary, purchased a 60% share of NuGeneration, with the intention of building three AP1000s at Moorside near the Sellafield nuclear reprocessing site in Cumbria, England, with a target first operation date of 2024.[71]

On 28 March 2017, the Office for Nuclear Regulation (ONR, UK) issued a Design Acceptance Confirmation for the AP1000 design, stating that 51 issues identified in 2011 had received an adequate response.[72][73] However, the following day the designer, Westinghouse, filed for Chapter 11 bankruptcy in the U.S. because of $9 billion of losses from its nuclear reactor construction projects, mostly the construction of four AP1000 reactors in the U.S.[74] In late 2017, Toshiba decided to sell its stake in NuGeneration, and the new owner will decide whether to continue the AP1000 project.[75]

India
See also: India–United States Civil Nuclear Agreement
In June 2016, the US and India agreed to build six AP1000 reactors in India as part of civil nuclear deal signed by both countries.[76] Negotiations are being conducted with the commercial contract expected to be signed by June 2017.[77] The proposed locations for the six-unit nuclear power plant is the coastal district of Gujarat; however, the site may be moved to the southeastern state of Andhra Pradesh, due to opposition from the local community.[78] Westinghouse's parent company Toshiba decided in 2017 to withdraw from the construction of nuclear power plants, following financial difficulties, leaving the proposed agreement in doubt.[79] During a visit to India in February 2020 by U.S. President Donald Trump, Westinghouse was expected to sign a new agreement with state-run Nuclear Power Corporation of India for the supply of six nuclear reactors[80]

Operations
In March 2019 Sanmen Unit 2 was shut down because of a reactor coolant pump[31] defect. A replacement pump has been shipped from the U.S. by Curtiss-Wright. There have been previous problems with these pumps, with several pumps returned from China. The pumps are the largest hermetically sealed pumps used in a nuclear reactor. Westinghouse and Curtiss-Wright are in a financial dispute over responsibility for the costs of pump delivery delays.[81][82]

See also
icon	Energy portal
	Nuclear technology portal
Nuclear safety in the United States
Nuclear power in the United States
Nuclear power in China
Nuclear power in the United Kingdom
Nuclear power in Bulgaria
Economics of nuclear power plants
Nuclear Power 2010 Program
References
 "Chinese AP1000s pass commissioning milestones". www.world-nuclear-news.org. 22 June 2018. Retrieved 23 June 2018.
 Gangloff, W. Westinghouse AP600 Advanced Nuclear Plant Design (PDF) (Technical report). IAEA.
 T.L. Schulz (2006). "Westinghouse AP1000 advanced passive plant". Nuclear Engineering and Design. 236 (14–16): 1547–1557. CiteSeerX 10.1.1.175.1734. doi:10.1016/j.nucengdes.2006.03.049.
 "AP 1000 Public Safety and Licensing". Westinghouse. 2004-09-13. Archived from the original (web) on 2007-08-07. Retrieved 2008-01-21.
 Wald, Matthew L. (2011-12-22). "N.R.C. Clears Way for Nuclear Plant Construction". The New York Times.
 "First new nuclear reactors OK'd in over 30 years". CNN. 2012-02-09.
 Mochizuki, Takashi. "Toshiba Expects Write-Down of as Much as Several Billion Dollars". Wall Street Journal. Retrieved 28 December 2016.
 Makiko Yamazaki, Taiga Uranaka (14 February 2017). "Delays, confusion as Toshiba reports $6.3 billion nuclear hit and slides to loss". Reuters. Retrieved 14 February 2017.
 "Toshiba chairman quits over nuclear loss". BBC News. 14 February 2017. Retrieved 14 February 2017.
 Karishma Vaswani (14 February 2017). "Toshiba: Why troubled Japanese firms survive". BBC News. Retrieved 14 February 2017.
 Fuse, Taro (24 March 2017). "Toshiba decides on Westinghouse bankruptcy, sees $9 billion in charges: sources". Reuters. Retrieved 25 March 2017.
 "Westinghouse emerges from Chapter 11 - World Nuclear News". www.world-nuclear-news.org. Retrieved 27 August 2018.
 Adrian Bull (16 November 2010), "The AP1000 Nuclear Power Plant - Global Experience and UK Prospects" (PDF), Westinghouse UK, Nuclear Institute, archived from the original (presentation) on 22 July 2011, retrieved 14 May 2011
 [1] Westinghouse AP 1000 Step 2 PSA Assessment
 Westinghouse certain of safety, efficiency of nuclear power, Pittsburgh Post-Gazette, March 29, 2009
 "UK AP1000 Pre-Construction Safety Report" (PDF). UKP-GW-GL-732 Revision 2 explains the design of the reactor safety systems as part of the process of seeking approval for construction in the UK. Westinghouse Electric Company. Archived from the original (PDF) on 2011-07-17. Retrieved 2010-02-23.
 R.A. and Worrall, A. “The AP1000 Reactor the Nuclear Renaissance Option.” Nuclear Energy 2004.
 "NRC: Issued Design Certification - Advanced Passive 1000 (AP1000)". www.nrc.gov.
 "Issued Design Certification - Advanced Passive 1000 (AP1000), Rev. 15 Design Certification Rule for the AP1000 Design".
 "Design Certification Application Review - AP1000 Amendment".
 "Groups say new Vogyle Reactors need study". August Chronicle. Archived from the original on 2011-07-07. Retrieved 2010-04-24.
 Matthew L. Wald. Critics Challenge Safety of New Reactor Design New York Times, April 22, 2010.
 Piore, Adam (June 2011). "Nuclear energy: Planning for the Black Swan". Scientific American.
 Robynne Boyd. Safety Concerns Delay Approval of the First U.S. Nuclear Reactor in Decades. Scientific American, July 29, 2010.
 Matthew L. Wald (March 2011). "Reactor Design Edges Toward Approval, but Not Without Complaints". The New York Times Company. Retrieved 15 May 2014.
 AP1000 containment insufficient for DBA, engineer claims Archived June 13, 2011, at the Wayback Machine Nuclear Engineering International, 29 April 2010.
 ACRS Concludes AP1000 Maintains Robustness of Previously Certified Design and is Safe Archived October 8, 2011, at the Wayback Machine Westinghouse. Retrieved 2011-11-04.
 Matthew L. Wald, Washington DC, “Regulators Find Design Flaws in New Reactors” New York Times, 20 May 2011.
 “Fukushima and the Westinghouse-Toshiba AP1000: A Report for The AP1000 Oversight Group” Arnie Gundersen, November 10, 2011
 "Sunday Dialogue: Nuclear Energy, Pro and Con". New York Times. February 25, 2012.
 "The world's largest canned motor pump". Nuclear Engineering International. 1 January 2013. Retrieved 23 July 2019.
 "China nuclear plant delay raises safety concern" Eric Ng, 7 October 2013, published in South China Morning Post
 "Nuclear Power in China". World Nuclear Association. 2 July 2010. Archived from the original on 31 July 2010. Retrieved 18 July 2010.
 Lin Tian (27 June 2013). "CAP 1400 Design & Construction" (PDF). SNPTC. IAEA. Retrieved 20 September 2016.
 "CAP1400 preliminary safety review approved". World Nuclear News. 9 September 2014. Retrieved 10 September 2014.
 "Large-scale Chinese reactor design passes IAEA safety review". World Nuclear News. 5 May 2016. Retrieved 20 September 2016.
 "New reactor design taking shape in China". World Nuclear News. 15 January 2014. Retrieved 16 January 2014.
 "China looks forward to reactor firsts". World Nuclear News. 14 September 2015. Retrieved 24 September 2015.
 Liao Liang (September 2015). Introduction of CAP1400 (PDF). SNERDI (Report). IAEA. Retrieved 24 February 2016.
 "CAP1400 reactor vessel passes pressure tests". World Nuclear News. 22 March 2017. Retrieved 22 March 2017.
 "上海核工院召开专家技术咨询会". 上海核电办公室. Retrieved 24 August 2019.
 "Second Summer AP1000 under construction". World Nuclear News. 6 November 2013.
 "Second Sanmen AP1000 connected to grid". World Nuclear News. 24 August 2018. Retrieved 27 August 2018.
 "China's Haiyang-1 Becomes Second Westinghouse AP1000 to Begin Commercial Operation".
 "Fourth Chinese AP1000 enters commercial operation". World Nuclear News. 9 January 2019. Retrieved 9 January 2019.
 "China produces first AP1000 vessel". World Nuclear News. 11 June 2014. Retrieved 6 August 2014.
 Mark Hibbs (April 27, 2010), "Pakistan Deal Signals China's Growing Nuclear Assertiveness", Nuclear Energy Brief, Carnegie Endowment for International Peace, archived from the original on 17 January 2011, retrieved 25 February 2011
 Li Qiyan (September 11, 2008). "U.S. Technology Picked for Nuclear Plants". Caijing. Archived from the original on 2008-10-15. Retrieved 2008-10-29.
 "Permits issued for construction of new Chinese plant". World Nuclear News. 15 October 2019. Retrieved 15 October 2019.
 Southern Company. "Plant Vogtle 3 and 4". Retrieved 2017-08-29.
 Westinghouse (2013). "AP1000 Construction Project Updates - VC Summer". Archived from the original on 2013-10-19.
 "Scana to evaluate Summer options". www.world-nuclear-news.org. 30 March 2017. Retrieved 11 April 2018.
 SCANA (2013). "Nuclear Financial Information".
 "The Augusta Chronicle: Local & World News, Sports & Entertainment in Augusta, GA". The Augusta Chronicle.
 Terry Macalister (10 April 2008). "Westinghouse wins first US nuclear deal in 30 years". The Guardian. London. Archived from the original on 11 April 2008. Retrieved 2008-04-09.
 "Georgia Power to Expand Nuclear Plant". Associated Press. Archived from the original on 2008-04-13. Retrieved 2008-04-09.
 "NRC: Combined License Application Documents for Vogtle, Units 3 and 4 Application". NRC. Archived from the original on 2011-07-21. Retrieved 2011-03-11.
 "Obama Administration Announces Loan Guarantees to Construct New Nuclear Power Reactors in Georgia". The White House Office of the Press Secretary. Archived from the original on 2010-05-01. Retrieved 2010-04-30.
 Rob Pavey (May 11, 2012). "Price of Vogtle expansion could increase $900 million". The Augusta Chronicle. Retrieved July 25, 2012.
 Rob Pavey (April 6, 2011). "Groups want licensing of reactors suspended". Augusta Chronicle.
 "NRC Approves Vogtle Reactor Construction". Nuclear Street. Retrieved 2012-02-09.
 "Cost of Summer AP1000s increases". World Nuclear News. 3 October 2014. Retrieved 6 October 2014.
 “China set to supply components to US nuclear power plants.” Lucy Hornby (Beijing) and Ed Crooks (New York), Financial Times, 30 October 2013 “Analysis - China needs Western help for nuclear export ambitions” David Stanway (Beijing) Reuters, 17 December 2013
 "Terms of Service Violation". www.bloomberg.com.
 http://m3web.bg, M3 Web -. "Bulgaria Seeks US Technology for New Unit of Kozloduy NPP - Novinite.com - Sofia News Agency".
 Tsolova, Tsvetelia (11 December 2013). "UPDATE 1-Bulgaria to start talks with Toshiba over new nuclear unit". Reuters.
 "WSJ: Westinghouse Electric in Talks With Bulgaria to Build Nuclear Reactor - Deal Could Be Worth Several Billion Dollars". Archived from the original on 2013-12-15. Retrieved 2013-12-15.
 http://m3web.bg, M3 Web -. "Bulgaria, Westinghouse Ink Deal on Kozloduy NPP - Novinite.com - Sofia News Agency".
 "Kozloduy NPP – Construction of unit 7: Expert Statement to the Environmental Impact Assessment Report" Andrea Wallner, Helmut Hirsch Adhipati Y. Indradiningrat, Oda Becker, Mathias Brettner Environment Agency Austria, 2013
 "FOCUS Information Agency". FOCUS Information Agency.
 "First AP1000 at Moorside online by 2024, Westinghouse says". Nuclear Engineering International. 14 January 2014. Retrieved 15 January 2014.
 "AP1000 design completes UK regulatory assessment". World Nuclear News. 30 March 2017. Retrieved 8 April 2017.
 "New nuclear power stations: Generic Design Assessment: Design Acceptance Confirmation for the AP1000® Reactor" (PDF). ONR. 28 March 2017. Retrieved 8 April 2017.
 "Westinghouse files for bankruptcy". Nuclear Engineering International. 29 March 2017. Retrieved 4 April 2017.
 "Kepco named preferred bidder for UK's NuGen". World Nuclear News. 7 December 2017. Retrieved 8 December 2017.
 IANS (8 June 2016). "N-joy: US firm to finally start work on nuclear power plants in India". Business Standard India – via Business Standard.
 "Westinghouse AP1000 reactors: Patchy record, cost concerns loom large". The Indian Express. 2016-06-22. Retrieved 2016-10-31.
 Belgium, Central Office, NucNet a.s.b.l., Brussels. "Preparatory Work 'To Begin Immediately' For Six Westinghouse AP1000 Reactors In India". www.nucnet.org. Retrieved 2016-10-31.
 Chakraborty, Nitya (10 February 2017). "India-US N-deal Under Threat". Millinium Post. Retrieved 24 February 2017.
 "Exclusive: Westinghouse set to sign pact with Indian firm for nuclear reactors during Trump visit". 20 February 2020. Retrieved 1 March 2020.
 "US-designed Chinese nuclear reactor forced to shut by pump defect". Platts. S&P Global. 14 March 2019. Retrieved 23 July 2019.
 "Curtiss-Wright Provides Update on AP1000 Reactor Coolant Pumps". Business Wire. 1 April 2019. Retrieved 23 July 2019.
External links
"AP1000: The Nuclear Renaissance Starts Here" (PDF). Archived from the original (PDF) on 2014-07-23. Retrieved 2015-07-08. (Westinghouse AP1000 brochure).
The AP1000 advanced 1000 MWe nuclear power plant
AP1000 design review documents Revision 14.
Fairewinds Associates Presentation AP1000 - extra risk of containment failure
vte
Types of nuclear fission reactor
vte
Westinghouse
vte
Toshiba
Categories: Nuclear power stations using AP1000 reactorsNuclear power reactor typesNuclear energy in ChinaNuclear energy in the United StatesNuclear energy in BulgariaNuclear energy in the United Kingdom"""
s="""X-ray
From Wikipedia, the free encyclopedia
Jump to navigationJump to search
This article is about the nature, production, and uses of the radiation. For the method of imaging, see Radiography. For the medical specialty, see Radiology. For other meanings, see X-ray (disambiguation).
Not to be confused with X-wave or X-band.

X-rays are part of the electromagnetic spectrum, with wavelengths shorter than visible light. Different applications use different parts of the X-ray spectrum.
X-ray
X-ray of human lungs
X-rays make up X-radiation, a form of high-energy electromagnetic radiation. Most X-rays have a wavelength ranging from 0.03 to 3 nanometres, corresponding to frequencies in the range 30 petahertz to 30 exahertz (3×1016 Hz to 3×1019 Hz) and energies in the range 100 eV to 200 keV. X-ray wavelengths are shorter than those of UV rays and typically longer than those of gamma rays. In many languages, X-radiation is referred to as Röntgen radiation, after the German scientist Wilhelm Röntgen, who discovered it on November 8, 1895.[1] He named it X-radiation to signify an unknown type of radiation.[2] Spellings of X-ray(s) in English include the variants x-ray(s), xray(s), and X ray(s).[3]


Contents
1	History
1.1	Pre-Röntgen observations and research
1.2	Discovery by Röntgen
1.3	Advances in radiology
1.4	Hazards discovered
1.5	20th century and beyond
2	Energy ranges
2.1	Soft and hard X-rays
2.2	Gamma rays
3	Properties
4	Interaction with matter
4.1	Photoelectric absorption
4.2	Compton scattering
4.3	Rayleigh scattering
5	Production
5.1	Production by electrons
5.2	Production by fast positive ions
5.3	Production in lightning and laboratory discharges
6	Detectors
7	Medical uses
7.1	Projectional radiographs
7.2	Computed tomography
7.3	Fluoroscopy
7.4	Radiotherapy
8	Adverse effects
9	Other uses
10	Visibility
11	Units of measure and exposure
12	See also
13	References
14	External links
History
Pre-Röntgen observations and research

Example of a Crookes Tube, a type of discharge tube that emitted X-rays
Before their discovery in 1895, X-rays were just a type of unidentified radiation emanating from experimental discharge tubes. They were noticed by scientists investigating cathode rays produced by such tubes, which are energetic electron beams that were first observed in 1869. Many of the early Crookes tubes (invented around 1875) undoubtedly radiated X-rays, because early researchers noticed effects that were attributable to them, as detailed below. Crookes tubes created free electrons by ionization of the residual air in the tube by a high DC voltage of anywhere between a few kilovolts and 100 kV. This voltage accelerated the electrons coming from the cathode to a high enough velocity that they created X-rays when they struck the anode or the glass wall of the tube.[4]

The earliest experimenter thought to have (unknowingly) produced X-rays was actuary William Morgan. In 1785 he presented a paper to the Royal Society of London describing the effects of passing electrical currents through a partially evacuated glass tube, producing a glow created by X-rays.[5][6] This work was further explored by Humphry Davy and his assistant Michael Faraday.

When Stanford University physics professor Fernando Sanford created his "electric photography" he also unknowingly generated and detected X-rays. From 1886 to 1888 he had studied in the Hermann Helmholtz laboratory in Berlin, where he became familiar with the cathode rays generated in vacuum tubes when a voltage was applied across separate electrodes, as previously studied by Heinrich Hertz and Philipp Lenard. His letter of January 6, 1893 (describing his discovery as "electric photography") to The Physical Review was duly published and an article entitled Without Lens or Light, Photographs Taken With Plate and Object in Darkness appeared in the San Francisco Examiner.[7]

Starting in 1888, Philipp Lenard conducted experiments to see whether cathode rays could pass out of the Crookes tube into the air. He built a Crookes tube with a "window" in the end made of thin aluminum, facing the cathode so the cathode rays would strike it (later called a "Lenard tube"). He found that something came through, that would expose photographic plates and cause fluorescence. He measured the penetrating power of these rays through various materials. It has been suggested that at least some of these "Lenard rays" were actually X-rays.[8]

In 1889 Ukrainian-born Ivan Pulyui, a lecturer in experimental physics at the Prague Polytechnic who since 1877 had been constructing various designs of gas-filled tubes to investigate their properties, published a paper on how sealed photographic plates became dark when exposed to the emanations from the tubes.[9]

Hermann von Helmholtz formulated mathematical equations for X-rays. He postulated a dispersion theory before Röntgen made his discovery and announcement. It was formed on the basis of the electromagnetic theory of light.[10] However, he did not work with actual X-rays.

In 1894 Nikola Tesla noticed damaged film in his lab that seemed to be associated with Crookes tube experiments and began investigating this radiant energy of "invisible" kinds.[11][12] After Röntgen identified the X-ray, Tesla began making X-ray images of his own using high voltages and tubes of his own design,[13] as well as Crookes tubes.

Discovery by Röntgen

Wilhelm Röntgen
On November 8, 1895, German physics professor Wilhelm Röntgen stumbled on X-rays while experimenting with Lenard tubes and Crookes tubes and began studying them. He wrote an initial report "On a new kind of ray: A preliminary communication" and on December 28, 1895 submitted it to Würzburg's Physical-Medical Society journal.[14] This was the first paper written on X-rays. Röntgen referred to the radiation as "X", to indicate that it was an unknown type of radiation. The name stuck, although (over Röntgen's great objections) many of his colleagues suggested calling them Röntgen rays. They are still referred to as such in many languages, including German, Hungarian, Danish, Polish, Bulgarian, Swedish, Finnish, Estonian, Russian, Japanese, Dutch, Georgian, Hebrew and Norwegian. Röntgen received the first Nobel Prize in Physics for his discovery.[15]

There are conflicting accounts of his discovery because Röntgen had his lab notes burned after his death, but this is a likely reconstruction by his biographers:[16][17] Röntgen was investigating cathode rays from a Crookes tube which he had wrapped in black cardboard so that the visible light from the tube would not interfere, using a fluorescent screen painted with barium platinocyanide. He noticed a faint green glow from the screen, about 1 meter away. Röntgen realized some invisible rays coming from the tube were passing through the cardboard to make the screen glow. He found they could also pass through books and papers on his desk. Röntgen threw himself into investigating these unknown rays systematically. Two months after his initial discovery, he published his paper.[18]


Hand mit Ringen (Hand with Rings): print of Wilhelm Röntgen's first "medical" X-ray, of his wife's hand, taken on 22 December 1895 and presented to Ludwig Zehnder of the Physik Institut, University of Freiburg, on 1 January 1896[19][20]
Röntgen discovered their medical use when he made a picture of his wife's hand on a photographic plate formed due to X-rays. The photograph of his wife's hand was the first photograph of a human body part using X-rays. When she saw the picture, she said "I have seen my death."[21]

The discovery of X-rays stimulated a veritable sensation. Röntgen's biographer Otto Glasser estimated that, in 1896 alone, as many as 49 essays and 1044 articles about the new rays were published.[22] This was probably a conservative estimate, if one considers that nearly every paper around the world extensively reported about the new discovery, with a magazine such as Science dedicating as many as 23 articles to it in that year alone.[23] Sensationalist reactions to the new discovery included publications linking the new kind of rays to occult and paranormal theories, such as telepathy.[24][25]

Advances in radiology

Taking an X-ray image with early Crookes tube apparatus, late 1800s. The Crookes tube is visible in center. The standing man is viewing his hand with a fluoroscope screen. The seated man is taking a radiograph of his hand by placing it on a photographic plate. No precautions against radiation exposure are taken; its hazards were not known at the time.

Surgical removal of a bullet whose location was diagnosed with X-rays (see inset) in 1897
Röntgen immediately noticed X-rays could have medical applications. Along with his 28 December Physical-Medical Society submission he sent a letter to physicians he knew around Europe (January 1, 1896).[26] News (and the creation of "shadowgrams") spread rapidly with Scottish electrical engineer Alan Archibald Campbell-Swinton being the first after Röntgen to create an X-ray (of a hand). Through February there were 46 experimenters taking up the technique in North America alone.[26]

The first use of X-rays under clinical conditions was by John Hall-Edwards in Birmingham, England on 11 January 1896, when he radiographed a needle stuck in the hand of an associate. On February 14, 1896 Hall-Edwards was also the first to use X-rays in a surgical operation.[27] In early 1896, several weeks after Röntgen's discovery, Ivan Romanovich Tarkhanov irradiated frogs and insects with X-rays, concluding that the rays "not only photograph, but also affect the living function".[28]

The first medical X-ray made in the United States was obtained using a discharge tube of Pulyui's design. In January 1896, on reading of Röntgen's discovery, Frank Austin of Dartmouth College tested all of the discharge tubes in the physics laboratory and found that only the Pulyui tube produced X-rays. This was a result of Pulyui's inclusion of an oblique "target" of mica, used for holding samples of fluorescent material, within the tube. On 3 February 1896 Gilman Frost, professor of medicine at the college, and his brother Edwin Frost, professor of physics, exposed the wrist of Eddie McCarthy, whom Gilman had treated some weeks earlier for a fracture, to the X-rays and collected the resulting image of the broken bone on gelatin photographic plates obtained from Howard Langill, a local photographer also interested in Röntgen's work.[29]


1896 plaque published in "Nouvelle Iconographie de la Salpetrière", a medical journal. In the left a hand deformity, in the right same hand seen using radiography. The authors named the technique Röntgen photography.
Many experimenters, including Röntgen himself in his original experiments, came up with methods to view X-ray images "live" using some form of luminescent screen.[26] Röntgen used a screen coated with barium platinocyanide. On February 5, 1896 live imaging devices were developed by both Italian scientist Enrico Salvioni (his "cryptoscope") and Professor McGie of Princeton University (his "Skiascope"), both using barium platinocyanide. American inventor Thomas Edison started research soon after Röntgen's discovery and investigated materials' ability to fluoresce when exposed to X-rays, finding that calcium tungstate was the most effective substance. In May 1896 he developed the first mass-produced live imaging device, his "Vitascope", later called the fluoroscope, which became the standard for medical X-ray examinations.[26] Edison dropped X-ray research around 1903, before the death of Clarence Madison Dally, one of his glassblowers. Dally had a habit of testing X-ray tubes on his own hands, developing a cancer in them so tenacious that both arms were amputated in a futile attempt to save his life; in 1904, he became the first known death attributed to X-ray exposure.[26] During the time the fluoroscope was being developed, Serbian American physicist Mihajlo Pupin, using a calcium tungstate screen developed by Edison, found that using a fluorescent screen decreased the exposure time it took to create a X-ray for medical imaging from an hour to a few minutes.[30][26]

In 1901, U.S. President William McKinley was shot twice in an assassination attempt. While one bullet only grazed his sternum, another had lodged somewhere deep inside his abdomen and could not be found. A worried McKinley aide sent word to inventor Thomas Edison to rush an X-ray machine to Buffalo to find the stray bullet. It arrived but was not used. While the shooting itself had not been lethal, gangrene had developed along the path of the bullet, and McKinley died of septic shock due to bacterial infection six days later.[31]

Hazards discovered
With the widespread experimentation with x‑rays after their discovery in 1895 by scientists, physicians, and inventors came many stories of burns, hair loss, and worse in technical journals of the time. In February 1896, Professor John Daniel and Dr. William Lofland Dudley of Vanderbilt University reported hair loss after Dr. Dudley was X-rayed. A child who had been shot in the head was brought to the Vanderbilt laboratory in 1896. Before trying to find the bullet an experiment was attempted, for which Dudley "with his characteristic devotion to science"[32][33][34] volunteered. Daniel reported that 21 days after taking a picture of Dudley's skull (with an exposure time of one hour), he noticed a bald spot 2 inches (5.1 cm) in diameter on the part of his head nearest the X-ray tube: "A plate holder with the plates towards the side of the skull was fastened and a coin placed between the skull and the head. The tube was fastened at the other side at a distance of one-half inch from the hair."[35]

In August 1896 Dr. HD. Hawks, a graduate of Columbia College, suffered severe hand and chest burns from an x-ray demonstration. It was reported in Electrical Review and led to many other reports of problems associated with x-rays being sent in to the publication.[36] Many experimenters including Elihu Thomson at Edison's lab, William J. Morton, and Nikola Tesla also reported burns. Elihu Thomson deliberately exposed a finger to an x-ray tube over a period of time and suffered pain, swelling, and blistering.[37] Other effects were sometimes blamed for the damage including ultraviolet rays and (according to Tesla) ozone.[38] Many physicians claimed there were no effects from X-ray exposure at all.[37] On August 3, 1905 at San Francisco, California, Elizabeth Fleischman, American X-ray pioneer, died from complications as a result of her work with X-rays.[39][40][41]

20th century and beyond

A patient being examined with a thoracic fluoroscope in 1940, which displayed continuous moving images. This image was used to argue that radiation exposure during the X-ray procedure would be negligible.
The many applications of X-rays immediately generated enormous interest. Workshops began making specialized versions of Crookes tubes for generating X-rays and these first-generation cold cathode or Crookes X-ray tubes were used until about 1920.

A typical early 20th century medical x-ray system consisted of a Ruhmkorff coil connected to a cold cathode Crookes X-ray tube. A spark gap was typically connected to the high voltage side in parallel to the tube and used for diagnostic purposes.[42] The spark gap allowed detecting the polarity of the sparks, measuring voltage by the length of the sparks thus determining the "hardness" of the vacuum of the tube, and it provided a load in the event the X-ray tube was disconnected. To detect the hardness of the tube, the spark gap was initially opened to the widest setting. While the coil was operating, the operator reduced the gap until sparks began to appear. A tube in which the spark gap began to spark at around 2 1/2 inches was considered soft (low vacuum) and suitable for thin body parts such as hands and arms. A 5 inch spark indicated the tube was suitable for shoulders and knees. A 7-9 inch spark would indicate a higher vacuum suitable for imaging the abdomen of larger individuals. Since the spark gap was connected in parallel to the tube, the spark gap had to be opened until the sparking ceased in order to operate the tube for imaging. Exposure time for photographic plates was around half a minute for a hand to a couple of minutes for a thorax. The plates may have a small addition of fluorescent salt to reduce exposure times.[42]

Crookes tubes were unreliable. They had to contain a small quantity of gas (invariably air) as a current will not flow in such a tube if they are fully evacuated. However, as time passed, the X-rays caused the glass to absorb the gas, causing the tube to generate "harder" X-rays until it soon stopped operating. Larger and more frequently used tubes were provided with devices for restoring the air, known as "softeners". These often took the form of a small side tube which contained a small piece of mica, a mineral that traps relatively large quantities of air within its structure. A small electrical heater heated the mica, causing it to release a small amount of air, thus restoring the tube's efficiency. However, the mica had a limited life, and the restoration process was difficult to control.

In 1904, John Ambrose Fleming invented the thermionic diode, the first kind of vacuum tube. This used a hot cathode that caused an electric current to flow in a vacuum. This idea was quickly applied to X-ray tubes, and hence heated-cathode X-ray tubes, called "Coolidge tubes", completely replaced the troublesome cold cathode tubes by about 1920.

In about 1906, the physicist Charles Barkla discovered that X-rays could be scattered by gases, and that each element had a characteristic X-ray spectrum. He won the 1917 Nobel Prize in Physics for this discovery.

In 1912, Max von Laue, Paul Knipping, and Walter Friedrich first observed the diffraction of X-rays by crystals. This discovery, along with the early work of Paul Peter Ewald, William Henry Bragg, and William Lawrence Bragg, gave birth to the field of X-ray crystallography.

In 1913, Henry Moseley performed crystallography experiments with X-rays emanating from various metals and formulated Moseley's law which relates the frequency of the X-rays to the atomic number of the metal.

The Coolidge X-ray tube was invented the same year by William D. Coolidge. It made possible the continuous emissions of X-rays. Modern X-ray tubes are based on this design, often employing the use of rotating targets which allow for significantly higher heat dissipation than static targets, further allowing higher quantity X-ray output for use in high powered applications such as rotational CT scanners.


Chandra's image of the galaxy cluster Abell 2125 reveals a complex of several massive multimillion-degree-Celsius gas clouds in the process of merging.
The use of X-rays for medical purposes (which developed into the field of radiation therapy) was pioneered by Major John Hall-Edwards in Birmingham, England. Then in 1908, he had to have his left arm amputated because of the spread of X-ray dermatitis on his arm.[43]

In 1914 Marie Curie developed radiological cars to support soldiers injured in World War I. The cars would allow for rapid X-ray imaging of wounded soldiers so battlefield surgeons could quickly and more accurately operate.[44]

From the 1920s through to the 1950s, X-ray machines were developed to assist in the fitting of shoes and were sold to commercial shoe stores.[45][46][47] Concerns regarding the impact of frequent or poorly controlled use were expressed in the 1950s,[48][49] leading to the practice's eventual end that decade.[50]

The X-ray microscope was developed during the 1950s.

The Chandra X-ray Observatory, launched on July 23, 1999, has been allowing the exploration of the very violent processes in the universe which produce X-rays. Unlike visible light, which gives a relatively stable view of the universe, the X-ray universe is unstable. It features stars being torn apart by black holes, galactic collisions, and novae, and neutron stars that build up layers of plasma that then explode into space.

An X-ray laser device was proposed as part of the Reagan Administration's Strategic Defense Initiative in the 1980s, but the only test of the device (a sort of laser "blaster" or death ray, powered by a thermonuclear explosion) gave inconclusive results. For technical and political reasons, the overall project (including the X-ray laser) was de-funded (though was later revived by the second Bush Administration as National Missile Defense using different technologies).


Dog hip xray posterior view

Phase-contrast X-ray image of spider
Phase-contrast X-ray imaging refers to a variety of techniques that use phase information of a coherent X-ray beam to image soft tissues. It has become an important method for visualizing cellular and histological structures in a wide range of biological and medical studies. There are several technologies being used for X-ray phase-contrast imaging, all utilizing different principles to convert phase variations in the X-rays emerging from an object into intensity variations.[51][52] These include propagation-based phase contrast,[53] talbot interferometry,[52] refraction-enhanced imaging,[54] and X-ray interferometry.[55] These methods provide higher contrast compared to normal absorption-contrast X-ray imaging, making it possible to see smaller details. A disadvantage is that these methods require more sophisticated equipment, such as synchrotron or microfocus X-ray sources, X-ray optics, and high resolution X-ray detectors.

Energy ranges
Soft and hard X-rays
X-rays with high photon energies (above 5–10 keV, below 0.2–0.1 nm wavelength) are called hard X-rays, while those with lower energy (and longer wavelength) are called soft X-rays.[56] Due to their penetrating ability, hard X-rays are widely used to image the inside of objects, e.g., in medical radiography and airport security. The term X-ray is metonymically used to refer to a radiographic image produced using this method, in addition to the method itself. Since the wavelengths of hard X-rays are similar to the size of atoms, they are also useful for determining crystal structures by X-ray crystallography. By contrast, soft X-rays are easily absorbed in air; the attenuation length of 600 eV (~2 nm) X-rays in water is less than 1 micrometer.[57]

Gamma rays
There is no consensus for a definition distinguishing between X-rays and gamma rays. One common practice is to distinguish between the two types of radiation based on their source: X-rays are emitted by electrons, while gamma rays are emitted by the atomic nucleus.[58][59][60][61] This definition has several problems: other processes also can generate these high-energy photons, or sometimes the method of generation is not known. One common alternative is to distinguish X- and gamma radiation on the basis of wavelength (or, equivalently, frequency or photon energy), with radiation shorter than some arbitrary wavelength, such as 10−11 m (0.1 Å), defined as gamma radiation.[62] This criterion assigns a photon to an unambiguous category, but is only possible if wavelength is known. (Some measurement techniques do not distinguish between detected wavelengths.) However, these two definitions often coincide since the electromagnetic radiation emitted by X-ray tubes generally has a longer wavelength and lower photon energy than the radiation emitted by radioactive nuclei.[58] Occasionally, one term or the other is used in specific contexts due to historical precedent, based on measurement (detection) technique, or based on their intended use rather than their wavelength or source. Thus, gamma-rays generated for medical and industrial uses, for example radiotherapy, in the ranges of 6–20 MeV, can in this context also be referred to as X-rays.[63]

Properties

Ionizing radiation hazard symbol
X-ray photons carry enough energy to ionize atoms and disrupt molecular bonds. This makes it a type of ionizing radiation, and therefore harmful to living tissue. A very high radiation dose over a short period of time causes radiation sickness, while lower doses can give an increased risk of radiation-induced cancer. In medical imaging this increased cancer risk is generally greatly outweighed by the benefits of the examination. The ionizing capability of X-rays can be utilized in cancer treatment to kill malignant cells using radiation therapy. It is also used for material characterization using X-ray spectroscopy.


Attenuation length of X-rays in water showing the oxygen absorption edge at 540 eV, the energy−3 dependence of photoabsorption, as well as a leveling off at higher photon energies due to Compton scattering. The attenuation length is about four orders of magnitude longer for hard X-rays (right half) compared to soft X-rays (left half).
Hard X-rays can traverse relatively thick objects without being much absorbed or scattered. For this reason, X-rays are widely used to image the inside of visually opaque objects. The most often seen applications are in medical radiography and airport security scanners, but similar techniques are also important in industry (e.g. industrial radiography and industrial CT scanning) and research (e.g. small animal CT). The penetration depth varies with several orders of magnitude over the X-ray spectrum. This allows the photon energy to be adjusted for the application so as to give sufficient transmission through the object and at the same time provide good contrast in the image.

X-rays have much shorter wavelengths than visible light, which makes it possible to probe structures much smaller than can be seen using a normal microscope. This property is used in X-ray microscopy to acquire high resolution images, and also in X-ray crystallography to determine the positions of atoms in crystals.

Interaction with matter
X-rays interact with matter in three main ways, through photoabsorption, Compton scattering, and Rayleigh scattering. The strength of these interactions depends on the energy of the X-rays and the elemental composition of the material, but not much on chemical properties, since the X-ray photon energy is much higher than chemical binding energies. Photoabsorption or photoelectric absorption is the dominant interaction mechanism in the soft X-ray regime and for the lower hard X-ray energies. At higher energies, Compton scattering dominates.

Photoelectric absorption
The probability of a photoelectric absorption per unit mass is approximately proportional to Z3/E3, where Z is the atomic number and E is the energy of the incident photon.[64] This rule is not valid close to inner shell electron binding energies where there are abrupt changes in interaction probability, so called absorption edges. However, the general trend of high absorption coefficients and thus short penetration depths for low photon energies and high atomic numbers is very strong. For soft tissue, photoabsorption dominates up to about 26 keV photon energy where Compton scattering takes over. For higher atomic number substances this limit is higher. The high amount of calcium (Z = 20) in bones, together with their high density, is what makes them show up so clearly on medical radiographs.

A photoabsorbed photon transfers all its energy to the electron with which it interacts, thus ionizing the atom to which the electron was bound and producing a photoelectron that is likely to ionize more atoms in its path. An outer electron will fill the vacant electron position and produce either a characteristic X-ray or an Auger electron. These effects can be used for elemental detection through X-ray spectroscopy or Auger electron spectroscopy.

Compton scattering
Compton scattering is the predominant interaction between X-rays and soft tissue in medical imaging.[65] Compton scattering is an inelastic scattering of the X-ray photon by an outer shell electron. Part of the energy of the photon is transferred to the scattering electron, thereby ionizing the atom and increasing the wavelength of the X-ray. The scattered photon can go in any direction, but a direction similar to the original direction is more likely, especially for high-energy X-rays. The probability for different scattering angles are described by the Klein–Nishina formula. The transferred energy can be directly obtained from the scattering angle from the conservation of energy and momentum.

Rayleigh scattering
Rayleigh scattering is the dominant elastic scattering mechanism in the X-ray regime.[66] Inelastic forward scattering gives rise to the refractive index, which for X-rays is only slightly below 1.[67]

Production
Whenever charged particles (electrons or ions) of sufficient energy hit a material, X-rays are produced.

Production by electrons
Characteristic X-ray emission lines for some common anode materials.[68][69]
Anode
material	Atomic
number	Photon energy [keV]	Wavelength [nm]
Kα1	Kβ1	Kα1	Kβ1
W	74	59.3	67.2	0.0209	0.0184
Mo	42	17.5	19.6	0.0709	0.0632
Cu	29	8.05	8.91	0.154	0.139
Ag	47	22.2	24.9	0.0559	0.0497
Ga	31	9.25	10.26	0.134	0.121
In	49	24.2	27.3	0.0512	0.455

Spectrum of the X-rays emitted by an X-ray tube with a rhodium target, operated at 60 kV. The smooth, continuous curve is due to bremsstrahlung, and the spikes are characteristic K lines for rhodium atoms.
X-rays can be generated by an X-ray tube, a vacuum tube that uses a high voltage to accelerate the electrons released by a hot cathode to a high velocity. The high velocity electrons collide with a metal target, the anode, creating the X-rays.[70] In medical X-ray tubes the target is usually tungsten or a more crack-resistant alloy of rhenium (5%) and tungsten (95%), but sometimes molybdenum for more specialized applications, such as when softer X-rays are needed as in mammography. In crystallography, a copper target is most common, with cobalt often being used when fluorescence from iron content in the sample might otherwise present a problem.

The maximum energy of the produced X-ray photon is limited by the energy of the incident electron, which is equal to the voltage on the tube times the electron charge, so an 80 kV tube cannot create X-rays with an energy greater than 80 keV. When the electrons hit the target, X-rays are created by two different atomic processes:

Characteristic X-ray emission (X-ray electroluminescence): If the electron has enough energy, it can knock an orbital electron out of the inner electron shell of the target atom. After that, electrons from higher energy levels fill the vacancies, and X-ray photons are emitted. This process produces an emission spectrum of X-rays at a few discrete frequencies, sometimes referred to as spectral lines. Usually these are transitions from the upper shells to the K shell (called K lines), to the L shell (called L lines) and so on. If the transition is from 2p to 1s, it is called Kα, while if it is from 3p to 1s it is Kβ. The frequencies of these lines depend on the material of the target and are therefore called characteristic lines. The Kα line usually has greater intensity than the Kβ one and is more desirable in diffraction experiments. Thus the Kβ line is filtered out by a filter. The filter is usually made of a metal having one proton less than the anode material (e.g., Ni filter for Cu anode or Nb filter for Mo anode).
Bremsstrahlung: This is radiation given off by the electrons as they are scattered by the strong electric field near the high-Z (proton number) nuclei. These X-rays have a continuous spectrum. The frequency of bremsstrahlung is limited by the energy of incident electrons.
So, the resulting output of a tube consists of a continuous bremsstrahlung spectrum falling off to zero at the tube voltage, plus several spikes at the characteristic lines. The voltages used in diagnostic X-ray tubes range from roughly 20 kV to 150 kV and thus the highest energies of the X-ray photons range from roughly 20 keV to 150 keV.[71]

Both of these X-ray production processes are inefficient, with only about one percent of the electrical energy used by the tube converted into X-rays, and thus most of the electric power consumed by the tube is released as waste heat. When producing a usable flux of X-rays, the X-ray tube must be designed to dissipate the excess heat.

A specialized source of X-rays which is becoming widely used in research is synchrotron radiation, which is generated by particle accelerators. Its unique features are X-ray outputs many orders of magnitude greater than those of X-ray tubes, wide X-ray spectra, excellent collimation, and linear polarization.[72]

Short nanosecond bursts of X-rays peaking at 15-keV in energy may be reliably produced by peeling pressure-sensitive adhesive tape from its backing in a moderate vacuum. This is likely to be the result of recombination of electrical charges produced by triboelectric charging. The intensity of X-ray triboluminescence is sufficient for it to be used as a source for X-ray imaging.[73]

Production by fast positive ions
X-rays can also be produced by fast protons or other positive ions. The proton-induced X-ray emission or particle-induced X-ray emission is widely used as an analytical procedure. For high energies, the production cross section is proportional to Z12Z2−4, where Z1 refers to the atomic number of the ion, Z2 refers to that of the target atom.[74] An overview of these cross sections is given in the same reference.

Production in lightning and laboratory discharges
X-rays are also produced in lightning accompanying terrestrial gamma-ray flashes. The underlying mechanism is the acceleration of electrons in lightning related electric fields and the subsequent production of photons through Bremsstrahlung.[75] This produces photons with energies of some few keV and several tens of MeV.[76] In laboratory discharges with a gap size of approximately 1 meter length and a peak voltage of 1 MV, X-rays with a characteristic energy of 160 keV are observed.[77] A possible explanation is the encounter of two streamers and the production of high-energy run-away electrons;[78] however, microscopic simulations have shown that the duration of electric field enhancement between two streamers is too short to produce a significantly number of run-away electrons.[79] Recently, it has been proposed that air perturbations in the vicinity of streamers can facilitate the production of run-away electrons and hence of X-rays from discharges.[80][81]

Detectors
Main article: X-ray detector
X-ray detectors vary in shape and function depending on their purpose. Imaging detectors such as those used for radiography were originally based on photographic plates and later photographic film, but are now mostly replaced by various digital detector types such as image plates and flat panel detectors. For radiation protection direct exposure hazard is often evaluated using ionization chambers, while dosimeters are used to measure the radiation dose a person has been exposed to. X-ray spectra can be measured either by energy dispersive or wavelength dispersive spectrometers. For x-ray diffraction applications, such as x-ray crystallography, hybrid photon counting detectors are widely used.[82]

Medical uses

This section needs additional citations for verification. Please help improve this article by adding citations to reliable sources. Unsourced material may be challenged and removed.
Find sources: "X-ray" – news · newspapers · books · scholar · JSTOR (November 2017) (Learn how and when to remove this template message)

X-ray.

A chest radiograph of a female, demonstrating a hiatal hernia
Since Röntgen's discovery that X-rays can identify bone structures, X-rays have been used for medical imaging.[83] The first medical use was less than a month after his paper on the subject.[29] Up to 2010, five billion medical imaging examinations had been conducted worldwide.[84] Radiation exposure from medical imaging in 2006 made up about 50% of total ionizing radiation exposure in the United States.[85]

Projectional radiographs
Main article: Projectional radiography

Plain radiograph of the right knee
Projectional radiography is the practice of producing two-dimensional images using x-ray radiation. Bones contain much calcium, which due to its relatively high atomic number absorbs x-rays efficiently. This reduces the amount of X-rays reaching the detector in the shadow of the bones, making them clearly visible on the radiograph. The lungs and trapped gas also show up clearly because of lower absorption compared to tissue, while differences between tissue types are harder to see.

Projectional radiographs are useful in the detection of pathology of the skeletal system as well as for detecting some disease processes in soft tissue. Some notable examples are the very common chest X-ray, which can be used to identify lung diseases such as pneumonia, lung cancer, or pulmonary edema, and the abdominal x-ray, which can detect bowel (or intestinal) obstruction, free air (from visceral perforations) and free fluid (in ascites). X-rays may also be used to detect pathology such as gallstones (which are rarely radiopaque) or kidney stones which are often (but not always) visible. Traditional plain X-rays are less useful in the imaging of soft tissues such as the brain or muscle. One area where projectional radiographs are used extensively is in evaluating how an orthopedic implant, such as a knee, hip or shoulder replacement, is situated in the body with respect to the surrounding bone. This can be assessed in two dimensions from plain radiographs, or it can be assessed in three dimensions if a technique called '2D to 3D registration' is used. This technique purportedly negates projection errors associated with evaluating implant position from plain radiographs.[86][87]

Dental radiography is commonly used in the diagnoses of common oral problems, such as cavities.

In medical diagnostic applications, the low energy (soft) X-rays are unwanted, since they are totally absorbed by the body, increasing the radiation dose without contributing to the image. Hence, a thin metal sheet, often of aluminium, called an X-ray filter, is usually placed over the window of the X-ray tube, absorbing the low energy part in the spectrum. This is called hardening the beam since it shifts the center of the spectrum towards higher energy (or harder) x-rays.

To generate an image of the cardiovascular system, including the arteries and veins (angiography) an initial image is taken of the anatomical region of interest. A second image is then taken of the same region after an iodinated contrast agent has been injected into the blood vessels within this area. These two images are then digitally subtracted, leaving an image of only the iodinated contrast outlining the blood vessels. The radiologist or surgeon then compares the image obtained to normal anatomical images to determine whether there is any damage or blockage of the vessel.

Computed tomography

Head CT scan (transverse plane) slice -– a modern application of medical radiography
Computed tomography (CT scanning) is a medical imaging modality where tomographic images or slices of specific areas of the body are obtained from a large series of two-dimensional X-ray images taken in different directions.[88] These cross-sectional images can be combined into a three-dimensional image of the inside of the body and used for diagnostic and therapeutic purposes in various medical disciplines.

Fluoroscopy
Fluoroscopy is an imaging technique commonly used by physicians or radiation therapists to obtain real-time moving images of the internal structures of a patient through the use of a fluoroscope. In its simplest form, a fluoroscope consists of an X-ray source and a fluorescent screen, between which a patient is placed. However, modern fluoroscopes couple the screen to an X-ray image intensifier and CCD video camera allowing the images to be recorded and played on a monitor. This method may use a contrast material. Examples include cardiac catheterization (to examine for coronary artery blockages) and barium swallow (to examine for esophageal disorders and swallowing disorders).

Radiotherapy
The use of X-rays as a treatment is known as radiation therapy and is largely used for the management (including palliation) of cancer; it requires higher radiation doses than those received for imaging alone. X-rays beams are used for treating skin cancers using lower energy x-ray beams while higher energy beams are used for treating cancers within the body such as brain, lung, prostate, and breast.[89][90]

Adverse effects

Abdominal radiograph of a pregnant woman, a procedure that should be performed only after proper assessment of benefit versus risk

Deformity of hand due to an X-ray burn. These burns are accidents. X-rays were not shielded when they were first discovered and used, and people received radiation burns.
Diagnostic X-rays (primarily from CT scans due to the large dose used) increase the risk of developmental problems and cancer in those exposed.[91][92][93] X-rays are classified as a carcinogen by both the World Health Organization's International Agency for Research on Cancer and the U.S. government.[84][94] It is estimated that 0.4% of current cancers in the United States are due to computed tomography (CT scans) performed in the past and that this may increase to as high as 1.5-2% with 2007 rates of CT usage.[95]

Experimental and epidemiological data currently do not support the proposition that there is a threshold dose of radiation below which there is no increased risk of cancer.[96] However, this is under increasing doubt.[97] It is estimated that the additional radiation from diagnostic X-rays will increase the average person's cumulative risk of getting cancer by age 75 by 0.6–3.0%.[98] The amount of absorbed radiation depends upon the type of X-ray test and the body part involved.[99] CT and fluoroscopy entail higher doses of radiation than do plain X-rays.

To place the increased risk in perspective, a plain chest X-ray will expose a person to the same amount from background radiation that people are exposed to (depending upon location) every day over 10 days, while exposure from a dental X-ray is approximately equivalent to 1 day of environmental background radiation.[100] Each such X-ray would add less than 1 per 1,000,000 to the lifetime cancer risk. An abdominal or chest CT would be the equivalent to 2–3 years of background radiation to the whole body, or 4–5 years to the abdomen or chest, increasing the lifetime cancer risk between 1 per 1,000 to 1 per 10,000.[100] This is compared to the roughly 40% chance of a US citizen developing cancer during their lifetime.[101] For instance, the effective dose to the torso from a CT scan of the chest is about 5 mSv, and the absorbed dose is about 14 mGy.[102] A head CT scan (1.5mSv, 64mGy)[103] that is performed once with and once without contrast agent, would be equivalent to 40 years of background radiation to the head. Accurate estimation of effective doses due to CT is difficult with the estimation uncertainty range of about ±19% to ±32% for adult head scans depending upon the method used.[104]

The risk of radiation is greater to a fetus, so in pregnant patients, the benefits of the investigation (X-ray) should be balanced with the potential hazards to the fetus.[105][106] In the US, there are an estimated 62 million CT scans performed annually, including more than 4 million on children.[99] Avoiding unnecessary X-rays (especially CT scans) reduces radiation dose and any associated cancer risk.[107]

Medical X-rays are a significant source of man-made radiation exposure. In 1987, they accounted for 58% of exposure from man-made sources in the United States. Since man-made sources accounted for only 18% of the total radiation exposure, most of which came from natural sources (82%), medical X-rays only accounted for 10% of total American radiation exposure; medical procedures as a whole (including nuclear medicine) accounted for 14% of total radiation exposure. By 2006, however, medical procedures in the United States were contributing much more ionizing radiation than was the case in the early 1980s. In 2006, medical exposure constituted nearly half of the total radiation exposure of the U.S. population from all sources. The increase is traceable to the growth in the use of medical imaging procedures, in particular computed tomography (CT), and to the growth in the use of nuclear medicine.[85][108]

Dosage due to dental X-rays varies significantly depending on the procedure and the technology (film or digital). Depending on the procedure and the technology, a single dental X-ray of a human results in an exposure of 0.5 to 4 mrem. A full mouth series of X-rays may result in an exposure of up to 6 (digital) to 18 (film) mrem, for a yearly average of up to 40 mrem.[109][110][111][112][113][114][115]

Financial incentives have been shown to have a significant impact on X-ray use with doctors who are paid a separate fee for each X-ray providing more X-rays.[116]

Other uses
Other notable uses of X-rays include:


Each dot, called a reflection, in this diffraction pattern forms from the constructive interference of scattered X-rays passing through a crystal. The data can be used to determine the crystalline structure.
X-ray crystallography in which the pattern produced by the diffraction of X-rays through the closely spaced lattice of atoms in a crystal is recorded and then analysed to reveal the nature of that lattice. In the early 1990s, experiments were done in which layers a few atoms thick of two different materials were deposited in a Thue-Morse sequence. The resulting object was found to yield X-ray diffraction patterns.[117] A related technique, fiber diffraction, was used by Rosalind Franklin to discover the double helical structure of DNA.[118]
X-ray astronomy, which is an observational branch of astronomy, which deals with the study of X-ray emission from celestial objects.
X-ray microscopic analysis, which uses electromagnetic radiation in the soft X-ray band to produce images of very small objects.
X-ray fluorescence, a technique in which X-rays are generated within a specimen and detected. The outgoing energy of the X-ray can be used to identify the composition of the sample.
Industrial radiography uses X-rays for inspection of industrial parts, particularly welds.

Using X-ray for inspection and quality control: the differences in the structures of the die and bond wires reveal the left chip to be counterfeit.[119]
Authentication and quality control of packaged items.
Industrial CT (computed tomography), a process which uses X-ray equipment to produce three-dimensional representations of components both externally and internally. This is accomplished through computer processing of projection images of the scanned object in many directions.
Paintings are often X-rayed to reveal underdrawings and pentimenti, alterations in the course of painting or by later restorers. Many pigments such as lead white show well in radiographs.
X-ray spectromicroscopy has been used to analyse the reactions of pigments in paintings. For example, in analysing colour degradation in the paintings of van Gogh.[120]
Airport security luggage scanners use X-rays for inspecting the interior of luggage for security threats before loading on aircraft.
Border control truck scanners and domestic police departments use X-rays for inspecting the interior of trucks.

X-ray fine art photography of needlefish by Peter Dazeley
X-ray art and fine art photography, artistic use of X-rays, for example the works by Stane Jagodič
X-ray hair removal, a method popular in the 1920s but now banned by the FDA.[121]
Shoe-fitting fluoroscopes were popularized in the 1920s, banned in the US in the 1960s, banned in the UK in the 1970s, and even later in continental Europe.
Roentgen stereophotogrammetry is used to track movement of bones based on the implantation of markers
X-ray photoelectron spectroscopy is a chemical analysis technique relying on the photoelectric effect, usually employed in surface science.
Radiation implosion is the use of high energy X-rays generated from a fission explosion (an A-bomb) to compress nuclear fuel to the point of fusion ignition (an H-bomb).
Visibility
While generally considered invisible to the human eye, in special circumstances X-rays can be visible. Brandes, in an experiment a short time after Röntgen's landmark 1895 paper, reported after dark adaptation and placing his eye close to an X-ray tube, seeing a faint "blue-gray" glow which seemed to originate within the eye itself.[122] Upon hearing this, Röntgen reviewed his record books and found he too had seen the effect. When placing an X-ray tube on the opposite side of a wooden door Röntgen had noted the same blue glow, seeming to emanate from the eye itself, but thought his observations to be spurious because he only saw the effect when he used one type of tube. Later he realized that the tube which had created the effect was the only one powerful enough to make the glow plainly visible and the experiment was thereafter readily repeatable. The knowledge that X-rays are actually faintly visible to the dark-adapted naked eye has largely been forgotten today; this is probably due to the desire not to repeat what would now be seen as a recklessly dangerous and potentially harmful experiment with ionizing radiation. It is not known what exact mechanism in the eye produces the visibility: it could be due to conventional detection (excitation of rhodopsin molecules in the retina), direct excitation of retinal nerve cells, or secondary detection via, for instance, X-ray induction of phosphorescence in the eyeball with conventional retinal detection of the secondarily produced visible light.

Though X-rays are otherwise invisible, it is possible to see the ionization of the air molecules if the intensity of the X-ray beam is high enough. The beamline from the wiggler at the ID11 at the European Synchrotron Radiation Facility is one example of such high intensity.[123]

Units of measure and exposure
The measure of X-rays ionizing ability is called the exposure:

The coulomb per kilogram (C/kg) is the SI unit of ionizing radiation exposure, and it is the amount of radiation required to create one coulomb of charge of each polarity in one kilogram of matter.
The roentgen (R) is an obsolete traditional unit of exposure, which represented the amount of radiation required to create one electrostatic unit of charge of each polarity in one cubic centimeter of dry air. 1 roentgen= 2.58×10−4 C/kg.
However, the effect of ionizing radiation on matter (especially living tissue) is more closely related to the amount of energy deposited into them rather than the charge generated. This measure of energy absorbed is called the absorbed dose:

The gray (Gy), which has units of (joules/kilogram), is the SI unit of absorbed dose, and it is the amount of radiation required to deposit one joule of energy in one kilogram of any kind of matter.
The rad is the (obsolete) corresponding traditional unit, equal to 10 millijoules of energy deposited per kilogram. 100 rad= 1 gray.
The equivalent dose is the measure of the biological effect of radiation on human tissue. For X-rays it is equal to the absorbed dose.

The Roentgen equivalent man (rem) is the traditional unit of equivalent dose. For X-rays it is equal to the rad, or, in other words, 10 millijoules of energy deposited per kilogram. 100 rem = 1 Sv.
The sievert (Sv) is the SI unit of equivalent dose, and also of effective dose. For X-rays the "equivalent dose" is numerically equal to a Gray (Gy). 1 Sv= 1 Gy. For the "effective dose" of X-rays, it is usually not equal to the Gray (Gy).
Ionising radiation related quantities view ‧ talk ‧ edit
Quantity	Unit	Symbol	Derivation	Year	SI equivalence
Activity (A)	becquerel	Bq	s−1	1974	SI unit
curie	Ci	3.7 × 1010 s−1	1953	3.7×1010 Bq
rutherford	Rd	106 s−1	1946	1,000,000 Bq
Exposure (X)	coulomb per kilogram	C/kg	C⋅kg−1 of air	1974	SI unit
röntgen	R	esu / 0.001293 g of air	1928	2.58 × 10−4 C/kg
Absorbed dose (D)	gray	Gy	J⋅kg−1	1974	SI unit
erg per gram	erg/g	erg⋅g−1	1950	1.0 × 10−4 Gy
rad	rad	100 erg⋅g−1	1953	0.010 Gy
Equivalent dose (H)	sievert	Sv	J⋅kg−1 × WR	1977	SI unit
röntgen equivalent man	rem	100 erg⋅g−1 x WR	1971	0.010 Sv
See also
	Medical portal
icon	Physics portal
Backscatter X-ray
Detective quantum efficiency
High-energy X-rays
Macintyre's X-Ray Film – 1896 documentary radiography film
N ray
Neutron radiation
NuSTAR
Radiographer
Reflection (physics)
Resonant inelastic X-ray scattering (RIXS)
Small-angle X-ray scattering (SAXS)
The X-Rays – 1897 British short silent comedy film
X-ray absorption spectroscopy
X-ray marker
X-ray nanoprobe
X-ray reflectivity
X-ray vision
X-ray welding
References
 "X-Rays". Science Mission Directorate. NASA.
 Novelline, Robert (1997). Squire's Fundamentals of Radiology. Harvard University Press. 5th edition. ISBN 0-674-83339-2.
 "X-ray". Oxford English Dictionary (3rd ed.). Oxford University Press. September 2005. (Subscription or UK public library membership required.)
 Filler, Aaron (2009). "The History, Development and Impact of Computed Imaging in Neurological Diagnosis and Neurosurgery: CT, MRI, and DTI". Nature Precedings. doi:10.1038/npre.2009.3267.5..
 Morgan, William (1785-02-24). "Electrical Experiments Made in Order to Ascertain the Non-Conducting Power of a Perfect Vacuum, &c". Philosophical Transactions of the Royal Society. Royal Society of London. 75: 272–278.
 Anderson, J.G. (January 1945), "William Morgan and X-rays", Transactions of the Faculty of Actuaries, 17: 219–221, doi:10.1017/s0071368600003001
 Wyman, Thomas (Spring 2005). "Fernando Sanford and the Discovery of X-rays". "Imprint", from the Associates of the Stanford University Libraries: 5–15.
 Thomson, Joseph J. (1903). The Discharge of Electricity through Gasses. USA: Charles Scribner's Sons. pp. 182–186.
 Gaida, Roman; et al. (1997). "Ukrainian Physicist Contributes to the Discovery of X-Rays". Mayo Foundation for Medical Education and Research. Archived from the original on 2008-05-28. Retrieved 2008-04-06.
 Wiedmann's Annalen, Vol. XLVIII
 Hrabak, M.; Padovan, R. S.; Kralik, M; Ozretic, D; Potocki, K (2008). "Scenes from the past: Nikola Tesla and the discovery of X-rays". RadioGraphics. 28 (4): 1189–92. doi:10.1148/rg.284075206. PMID 18635636.
 Chadda, P. K. (2009). Hydroenergy and Its Energy Potential. Pinnacle Technology. pp. 88–. ISBN 978-1-61820-149-2.
 From his technical publications, it is indicated that he invented and developed a special single-electrode X-ray tube: Morton, William James and Hammer, Edwin W. (1896) American Technical Book Co., p. 68., U.S. Patent 514,170, "Incandescent Electric Light", and U.S. Patent 454,622 "System of Electric Lighting". These differed from other X-ray tubes in having no target electrode and worked with the output of a Tesla Coil.
 Stanton, Arthur (1896-01-23). "Wilhelm Conrad Röntgen On a New Kind of Rays: translation of a paper read before the Würzburg Physical and Medical Society, 1895". Nature. 53 (1369): 274–6. Bibcode:1896Natur..53R.274.. doi:10.1038/053274b0. see also pp. 268 and 276 of the same issue.
 Karlsson, Erik B. (9 February 2000). "The Nobel Prizes in Physics 1901–2000". Stockholm: The Nobel Foundation. Retrieved 24 November 2011.
 Peters, Peter (1995). "W. C. Roentgen and the discovery of x-rays". Textbook of Radiology. Medcyclopedia.com, GE Healthcare. Archived from the original on 11 May 2008. Retrieved 5 May 2008.
 Glasser, Otto (1993). Wilhelm Conrad Röntgen and the early history of the roentgen rays. Norman Publishing. pp. 10–15. ISBN 978-0930405229.
 Arthur, Charles (2010-11-08). "Google doodle celebrates 115 years of X-rays". The Guardian. Guardian US. Retrieved 5 February 2019.
 Kevles, Bettyann Holtzmann (1996). Naked to the Bone Medical Imaging in the Twentieth Century. Camden, NJ: Rutgers University Press. pp. 19–22. ISBN 978-0-8135-2358-3.
 Sample, Sharro (2007-03-27). "X-Rays". The Electromagnetic Spectrum. NASA. Retrieved 2007-12-03.
 Markel, Howard (20 December 2012). "'I Have Seen My Death': How the World Discovered the X-Ray". PBS NewsHour. PBS. Retrieved 23 March 2019.
 Glasser, Otto (1958). Dr. W. C. Ro ̈ntgen. Springfield: Thomas.
 Natale, Simone (2011-11-01). "The Invisible Made Visible". Media History. 17 (4): 345–358. doi:10.1080/13688804.2011.602856. hdl:2134/19408.
 Natale, Simone (2011-08-04). "A Cosmology of Invisible Fluids: Wireless, X-Rays, and Psychical Research Around 1900". Canadian Journal of Communication. 36 (2). doi:10.22230/cjc.2011v36n2a2368.
 Grove, Allen W. (1997-01-01). "Rontgen's Ghosts: Photography, X-Rays, and the Victorian Imagination". Literature and Medicine. 16 (2): 141–173. doi:10.1353/lm.1997.0016.
 Feldman, A (1989). "A sketch of the technical history of radiology from 1896 to 1920". Radiographics. 9 (6): 1113–1128. doi:10.1148/radiographics.9.6.2685937. PMID 2685937.
 "Major John Hall-Edwards". Birmingham City Council. Archived from the original on September 28, 2012. Retrieved 2012-05-17.
 Kudriashov, Y. B. (2008). Radiation Biophysics. Nova Publishers. p. xxi. ISBN 9781600212802.
 Spiegel, P. K (1995). "The first clinical X-ray made in America—100 years". American Journal of Roentgenology. 164 (1): 241–243. doi:10.2214/ajr.164.1.7998549. PMID 7998549.
 Nicolaas A. Rupke, Eminent Lives in Twentieth-Century Science and Religion, page 300, Peter Lang, 2009 ISBN 3631581203
 National Library of Medicine. "Could X-rays Have Saved President William McKinley?" Visible Proofs: Forensic Views of the Body.
 Daniel, J. (April 10, 1896). "The X-Rays". Science. 3 (67): 562–563. Bibcode:1896Sci.....3..562D. doi:10.1126/science.3.67.562. PMID 17779817.
 Fleming, Walter Lynwood (1909). The South in the Building of the Nation: Biography A-J. Pelican Publishing. p. 300. ISBN 978-1589809468.
 Ce4Rt (Mar 2014). Understanding Ionizing Radiation and Protection. p. 174.
 Glasser, Otto (1934). Wilhelm Conrad Röntgen and the Early History of the Roentgen Rays. Norman Publishing. p. 294. ISBN 978-0930405229.
 Sansare K, Khanna V, Karjodkar F (2011). "Early victims of X-rays: A tribute and current perception". Dentomaxillofacial Radiology. 40 (2): 123–125. doi:10.1259/dmfr/73488299. PMC 3520298. PMID 21239576.
 Kathern, Ronald L. and Ziemer, Paul L. The First Fifty Years of Radiation Protection, physics.isu.edu
 Hrabak M, Padovan RS, Kralik M, Ozretic D, Potocki K (July 2008). "Nikola Tesla and the Discovery of X-rays". RadioGraphics. 28 (4): 1189–92. doi:10.1148/rg.284075206. PMID 18635636.
 California, San Francisco Area Funeral Home Records, 1835–1979. Database with images. FamilySearch. Jacob Fleischman in entry for Elizabeth Aschheim. 03 Aug 1905. Citing funeral home J.S. Godeau, San Francisco, San Francisco, California. Record book Vol. 06, p. 1-400, 1904–1906. San Francisco Public Library. San Francisco History and Archive Center.
 Editor. (August 5, 1905). Aschheim. Obituaries. San Francisco Examiner. San Francisco, California.
 Editor. (August 5, 1905). Obituary Notice. Elizabeth Fleischmann. San Francisco Chronicle. Page 10.
 Schall, K. (1905). Electro-medical Instruments and their Management. Bemrose & Sons Ltd. Printers. pp. 96, 107.
 Birmingham City Council: Major John Hall-Edwards Archived September 28, 2012, at the Wayback Machine
 Jorgensen, Timothy J. (10 October 2017). "Marie Curie and her X-ray vehicles' contribution to World War I battlefield medicine". The Conversation. Retrieved February 23, 2018.
 "T. C. BEIRNE'S X-RAY SHOE FITTING". Telegraph (Brisbane, Qld. : 1872–1947). 1925-07-17. p. 8. Retrieved 2017-11-05.
 "THE PEDOSCOPE". Sunday Times (Perth, WA : 1902–1954). 1928-07-15. p. 5. Retrieved 2017-11-05.
 "X-RAY SHOE FITTINGS". Biz (Fairfield, NSW : 1928–1972). 1955-07-27. p. 10. Retrieved 2017-11-05.
 "SHOE X-RAY DANGERS". Brisbane Telegraph (Qld. : 1948–1954). 1951-02-28. p. 7. Retrieved 2017-11-05.
 "X-ray shoe sets in S.A. 'controlled'". News (Adelaide, SA : 1923–1954). 1951-04-27. p. 12. Retrieved 2017-11-05.
 "Ban On Shoe X-ray Machines Resented". Canberra Times (ACT : 1926–1995). 1957-06-26. p. 4. Retrieved 2017-11-05.
 Fitzgerald, Richard (2000). "Phase-sensitive x-ray imaging". Physics Today. 53 (7): 23–26. Bibcode:2000PhT....53g..23F. doi:10.1063/1.1292471.
 David, C, Nohammer, B, Solak, H H, & Ziegler E (2002). "Differential x-ray phase contrast imaging using a shearing interferometer". Applied Physics Letters. 81 (17): 3287–3289. Bibcode:2002ApPhL..81.3287D. doi:10.1063/1.1516611.
 Wilkins, S W, Gureyev, T E, Gao, D, Pogany, A & Stevenson, A W (1996). "Phase-contrast imaging using polychromatic hard X-rays". Nature. 384 (6607): 335–338. Bibcode:1996Natur.384..335W. doi:10.1038/384335a0.
 Davis, T J, Gao, D, Gureyev, T E, Stevenson, A W & Wilkins, S W (1995). "Phase-contrast imaging of weakly absorbing materials using hard X-rays". Nature. 373 (6515): 595–598. Bibcode:1995Natur.373..595D. doi:10.1038/373595a0.
 Momose A, Takeda T, Itai Y, Hirano K (1996). "Phase-contrast X-ray computed tomography for observing biological soft tissues". Nature Medicine. 2 (4): 473–475. doi:10.1038/nm0496-473. PMID 8597962.
 Attwood, David (1999). Soft X-rays and extreme ultraviolet radiation. Cambridge University. p. 2. ISBN 978-0-521-65214-8. Archived from the original on 2012-11-11. Retrieved 2012-11-04.
 "Physics.nist.gov". Physics.nist.gov. Retrieved 2011-11-08.
 Denny, P. P.; Heaton, B. (1999). Physics for Diagnostic Radiology. USA: CRC Press. p. 12. ISBN 978-0-7503-0591-4.
 Feynman, Richard; Leighton, Robert; Sands, Matthew (1963). The Feynman Lectures on Physics, Vol.1. USA: Addison-Wesley. pp. 2–5. ISBN 978-0-201-02116-5.
 L'Annunziata, Michael; Abrade, Mohammad (2003). Handbook of Radioactivity Analysis. Academic Press. p. 58. ISBN 978-0-12-436603-9.
 Grupen, Claus; Cowan, G.; Eidelman, S. D.; Stroh, T. (2005). Astroparticle Physics. Springer. p. 109. ISBN 978-3-540-25312-9.
 Hodgman, Charles, ed. (1961). CRC Handbook of Chemistry and Physics, 44th Ed. USA: Chemical Rubber Co. p. 2850.
 Government of Canada, Canadian Centre for Occupational Health and Safety (2019-05-09). "Radiation – Quantities and Units of Ionizing Radiation : OSH Answers". www.ccohs.ca. Retrieved 2019-05-09.
 Bushberg, Jerrold T.; Seibert, J. Anthony; Leidholdt, Edwin M.; Boone, John M. (2002). The essential physics of medical imaging. Lippincott Williams & Wilkins. p. 42. ISBN 978-0-683-30118-2.
 Bushberg, Jerrold T.; Seibert, J. Anthony; Leidholdt, Edwin M.; Boone, John M. (2002). The essential physics of medical imaging. Lippincott Williams & Wilkins. p. 38. ISBN 978-0-683-30118-2.
 Kissel, Lynn (2000-09-02). "RTAB: the Rayleigh scattering database". Radiation Physics and Chemistry. Lynn Kissel. 59 (2): 185–200. Bibcode:2000RaPC...59..185K. doi:10.1016/S0969-806X(00)00290-5. Archived from the original on 2011-12-12. Retrieved 2012-11-08.
 Attwood, David (1999). "3". Soft X-rays and extreme ultraviolet radiation. Cambridge University Press. ISBN 978-0-521-65214-8. Archived from the original on 2012-11-11. Retrieved 2012-11-04.
 "X-ray Transition Energies Database". NIST Physical Measurement Laboratory. 2011-12-09. Retrieved 2016-02-19.
 "X-Ray Data Booklet Table 1-3" (PDF). Center for X-ray Optics and Advanced Light Source, Lawrence Berkeley National Laboratory. 2009-10-01. Archived from the original (PDF) on 23 April 2009. Retrieved 2016-02-19.
 Whaites, Eric; Cawson, Roderick (2002). Essentials of Dental Radiography and Radiology. Elsevier Health Sciences. pp. 15–20. ISBN 978-0-443-07027-3.
 Bushburg, Jerrold; Seibert, Anthony; Leidholdt, Edwin; Boone, John (2002). The Essential Physics of Medical Imaging. USA: Lippincott Williams & Wilkins. p. 116. ISBN 978-0-683-30118-2.
 Emilio, Burattini; Ballerna, Antonella (1994). "Preface". Biomedical Applications of Synchrotron Radiation: Proceedings of the 128th Course at the International School of Physics -Enrico Fermi- 12–22 July 1994, Varenna, Italy. IOS Press. p. xv. ISBN 90-5199-248-3.
 Camara, C. G.; Escobar, J. V.; Hird, J. R.; Putterman, S. J. (2008). "Correlation between nanosecond X-ray flashes and stick–slip friction in peeling tape" (PDF). Nature. 455 (7216): 1089–1092. Bibcode:2008Natur.455.1089C. doi:10.1038/nature07378. Retrieved 2 February 2013.
 Paul, Helmut; Muhr, Johannes (1986). "Review of experimental cross sections for K-shell ionization by light ions". Physics Reports. 135 (2): 47–97. doi:10.1016/0370-1573(86)90149-3.
 Köhn, Christoph; Ebert, Ute (2014). "Angular distribution of Bremsstrahlung photons and of positrons for calculations of terrestrial gamma-ray flashes and positron beams". Atmospheric Research. 135-136: 432–465. arXiv:1202.4879. Bibcode:2014AtmRe.135..432K. doi:10.1016/j.atmosres.2013.03.012.
 Köhn, Christoph; Ebert, Ute (2015). "Calculation of beams of positrons, neutrons, and protons associated with terrestrial gamma ray flashes". Journal of Geophysical Research: Atmospheres. 120 (4): 1620–1635. doi:10.1002/2014JD022229.
 Kochkin, Pavlo; Köhn, Christoph; Ebert, Ute; Van Deursen, Lex (2016). "Analyzing x-ray emissions from meter-scale negative discharges in ambient air". Plasma Sources Science and Technology. 25 (4): 044002. doi:10.1088/0963-0252/25/4/044002.
 Cooray, Vernon; Arevalo, Liliana; Rahman, Mahbubur; Dwyer, Joseph; Rassoul, Hamid (2009). "On the possible origin of X-rays in long laboratory sparks". Journal of Atmospheric and Solar-Terrestrial Physics. 71 (17–18): 1890–1898. doi:10.1016/j.jastp.2009.07.010.
 Köhn, C; Chanrion, O; Neubert, T (2017). "Electron acceleration during streamer collisions in air". Geophysical Research Letters. 44 (5): 2604–2613. doi:10.1002/2016GL072216. PMC 5405581. PMID 28503005.
 Köhn, C; Chanrion, O; Babich, L P; Neubert, T (2018). "Streamer properties and associated x-rays in perturbed air". Plasma Sources Science and Technology. 27: 015017. doi:10.1088/1361-6595/aaa5d8.
 Köhn, C; Chanrion, O; Neubert, T (2018). "High-Energy Emissions Induced by Air Density Fluctuations of Discharges". Geophysical Research Letters. 45 (10): 5194–5203. doi:10.1029/2018GL077788. PMC 6049893. PMID 30034044.
 Förster, A; Brandstetter, S; Schulze-Briese, C (2019). "Transforming X-ray detection with hybrid photon counting detectors". Philosophical Transactions of the Royal Society A: Mathematical, Physical and Engineering Sciences. 377 (2147): 20180241. doi:10.1098/rsta.2018.0241. PMC 6501887. PMID 31030653.
 "Roentgen's discovery of the x-ray". www.bl.uk. Retrieved 2019-05-09.
 Roobottom CA, Mitchell G, Morgan-Hughes G (2010). "Radiation-reduction strategies in cardiac computed tomographic angiography". Clin Radiol. 65 (11): 859–67. doi:10.1016/j.crad.2010.04.021. PMID 20933639. Of the 5 billion imaging investigations performed worldwide...
 Medical Radiation Exposure Of The U.S. Population Greatly Increased Since The Early 1980s, Science Daily, March 5, 2009
 Accuracy of total knee implant position assessment based on postoperative X-rays, registered to pre-operative CT-based 3D models. Annemieke van Haver, Sjoerd Kolk, Sebastian de Boodt, Kars Valkering, Peter Verdonk. Orthopaedic Proceedings, Published 20 February 2017. http://bjjprocs.boneandjoint.org.uk/content/99-B/SUPP_4/80
 Accuracy assessment of 2D X-ray to 3D CT registration for measuring 3D postoperative implant position. Lara Vigneron, Hendrik Delport, Sebastian de Boodt. White paper, Published 2014. http://www.materialise.com/en/system/files/uploads/resources/X-ray.pdf
 Herman, Gabor T. (2009). Fundamentals of Computerized Tomography: Image Reconstruction from Projections (2nd ed.). Springer. ISBN 978-1-85233-617-2.
 Advances in kilovoltage x-ray beam dosimetry in Hill R, Healy B, Holloway L, Kuncic Z, Thwaites D, Baldock C (2014). "Advances in kilovoltage x-ray beam dosimetry". Phys Med Biol. 59 (6): R183–231. Bibcode:2014PMB....59R.183H. doi:10.1088/0031-9155/59/6/r183. PMID 24584183.
 Thwaites David I (2006). "Back to the future: the history and development of the clinical linear accelerator". Physics in Medicine and Biology. 51 (13): R343–R362. Bibcode:2006PMB....51R.343T. doi:10.1088/0031-9155/51/13/R20. PMID 16790912.
 Hall EJ, Brenner DJ (2008). "Cancer risks from diagnostic radiology". Br J Radiol. 81 (965): 362–78. doi:10.1259/bjr/01948454. PMID 18440940.
 Brenner DJ (2010). "Should we be concerned about the rapid increase in CT usage?". Rev Environ Health. 25 (1): 63–8. doi:10.1515/REVEH.2010.25.1.63. PMID 20429161.
 De Santis M, Cesari E, Nobili E, Straface G, Cavaliere AF, Caruso A (2007). "Radiation effects on development". Birth Defects Res. C Embryo Today. 81 (3): 177–82. doi:10.1002/bdrc.20099. PMID 17963274.
 "11th Report on Carcinogens". Ntp.niehs.nih.gov. Archived from the original on 2010-12-09. Retrieved 2010-11-08.
 Brenner DJ, Hall EJ (2007). "Computed tomography—an increasing source of radiation exposure". N. Engl. J. Med. 357 (22): 2277–84. doi:10.1056/NEJMra072149. PMID 18046031.
 Upton AC (2003). "The state of the art in the 1990s: NCRP report No. 136 on the scientific bases for linearity in the dose-response relationship for ionizing radiation". Health Physics. 85 (1): 15–22. doi:10.1097/00004032-200307000-00005. PMID 12852466.
 Calabrese EJ, Baldwin LA (2003). "Toxicology rethinks its central belief" (PDF). Nature. 421 (6924): 691–2. Bibcode:2003Natur.421..691C. doi:10.1038/421691a. PMID 12610596. Archived from the original (PDF) on 2011-09-12.
 Berrington de González A, Darby S (2004). "Risk of cancer from diagnostic X-rays: estimates for the UK and 14 other countries". Lancet. 363 (9406): 345–351. doi:10.1016/S0140-6736(04)15433-0. PMID 15070562.
 Brenner DJ, Hall EJ (2007). "Computed tomography- an increasing source of radiation exposure". New England Journal of Medicine. 357 (22): 2277–2284. doi:10.1056/NEJMra072149. PMID 18046031.
 Radiologyinfo.org, Radiological Society of North America and American College of Radiology
 "National Cancer Institute: Surveillance Epidemiology and End Results (SEER) data". Seer.cancer.gov. 2010-06-30. Retrieved 2011-11-08.
 Caon, M., Bibbo, G. & Pattison, J. (2000). "Monte Carlo calculated effective dose to teenage girls from computed tomography examinations". Radiation Protection Dosimetry. 90 (4): 445–448. doi:10.1093/oxfordjournals.rpd.a033172.
 Shrimpton, P.C; Miller, H.C; Lewis, M.A; Dunn, M. Doses from Computed Tomography (CT) examinations in the UK – 2003 Review Archived September 22, 2011, at the Wayback Machine
 Gregory KJ, Bibbo G, Pattison JE (2008). "On the uncertainties in effective dose estimates of adult CT head scans". Medical Physics. 35 (8): 3501–10. Bibcode:2008MedPh..35.3501G. doi:10.1118/1.2952359. PMID 18777910.
 Giles D, Hewitt D, Stewart A, Webb J (1956). "Preliminary Communication: Malignant Disease in Childhood and Diagnostic Irradiation In-Utero". Lancet. 271 (6940): 447. doi:10.1016/S0140-6736(56)91923-7. PMID 13358242.
 "Pregnant Women and Radiation Exposure". eMedicine Live online medical consultation. Medscape. 28 December 2008. Archived from the original on January 23, 2009. Retrieved 2009-01-16.
 Donnelly LF (2005). "Reducing radiation dose associated with pediatric CT by decreasing unnecessary examinations". American Journal of Roentgenology. 184 (2): 655–7. doi:10.2214/ajr.184.2.01840655. PMID 15671393.
 US National Research Council (2006). Health Risks from Low Levels of Ionizing Radiation, BEIR 7 phase 2. National Academies Press. pp. 5, fig.PS–2. ISBN 978-0-309-09156-5., data credited to NCRP (US National Committee on Radiation Protection) 1987
 "ANS / Public Information / Resources / Radiation Dose Calculator".
 The Nuclear Energy Option, Bernard Cohen, Plenum Press 1990 Ch. 5 Archived November 20, 2013, at the Wayback Machine
 Muller, Richard. Physics for Future Presidents, Princeton University Press, 2010
 X-Rays Archived 2007-03-15 at the Wayback Machine. Doctorspiller.com (2007-05-09). Retrieved on 2011-05-05.
 X-Ray Safety Archived April 4, 2007, at the Wayback Machine. Dentalgentlecare.com (2008-02-06). Retrieved on 2011-05-05.
 "Dental X-Rays". Idaho State University. Retrieved November 7, 2012.
 D.O.E. – About Radiation Archived April 27, 2012, at the Wayback Machine
 Chalkley, M.; Listl, S. (30 December 2017). "First do no harm – The impact of financial incentives on dental X-rays". Journal of Health Economics. 58 (March 2018): 1–9. doi:10.1016/j.jhealeco.2017.12.005. PMID 29408150.
 Wolfram, Stephen (2002). A New Kind of Science. Champaign, Illinois: Wolfram Media, Inc. p. 586. ISBN 978-1579550080. Retrieved 15 March 2018.
 Kasai, Nobutami; Kakudo, Masao (2005). X-ray diffraction by macromolecules. Tokyo: Kodansha. pp. 291–2. ISBN 978-3-540-25317-4.
 Ahi, Kiarash (May 26, 2016). "Advanced terahertz techniques for quality control and counterfeit detection". Proc. SPIE 9856, Terahertz Physics, Devices, and Systems X: Advanced Applications in Industry and Defense, 98560G. Terahertz Physics, Devices, and Systems X: Advanced Applications in Industry and Defense. 9856: 98560G. Bibcode:2016SPIE.9856E..0GA. doi:10.1117/12.2228684. Retrieved May 26, 2016.
 Monico L, Van der Snickt G, Janssens K, De Nolf W, Miliani C, Verbeeck J, Tian H, Tan H, Dik J, Radepont M, Cotte M (2011). "Degradation Process of Lead Chromate in Paintings by Vincent van Gogh Studied by Means of Synchrotron X-ray Spectromicroscopy and Related Methods. 1. Artificially Aged Model Samples". Analytical Chemistry. 83 (4): 1214–1223. doi:10.1021/ac102424h. PMID 21314201. Monico L, Van der Snickt G, Janssens K, De Nolf W, Miliani C, Dik J, Radepont M, Hendriks E, Geldof M, Cotte M (2011). "Degradation Process of Lead Chromate in Paintings by Vincent van Gogh Studied by Means of Synchrotron X-ray Spectromicroscopy and Related Methods. 2. Original Paint Layer Samples" (PDF). Analytical Chemistry. 83 (4): 1224–1231. doi:10.1021/ac1025122. PMID 21314202.
 Bickmore, Helen (2003). Milady's Hair Removal Techniques: A Comprehensive Manual. ISBN 978-1401815554.
 Frame, Paul. "Wilhelm Röntgen and the Invisible Light". Tales from the Atomic Age. Oak Ridge Associated Universities. Retrieved 2008-05-19.
 Als-Nielsen, Jens; Mcmorrow, Des (2001). Elements of Modern X-Ray Physics. John Wiley & Sons Ltd. pp. 40–41. ISBN 978-0-471-49858-2.
External links
	Wikimedia Commons has media related to X-ray.
	Look up x-ray in Wiktionary, the free dictionary.
Historical X-ray tubes
Röntgen's 1895 article, on line and analyzed on BibNum [click 'à télécharger' for English analysis]
Example Radiograph: Fractured Humerus
A Photograph of an X-ray Machine
X-ray Safety
An X-ray tube demonstration (Animation)
1896 Article: "On a New Kind of Rays"
"Digital X-Ray Technologies Project"
What is Radiology? a simple tutorial
50,000 X-ray, MRI, and CT pictures MedPix medical image database
Index of Early Bremsstrahlung Articles
Extraordinary X-Rays – slideshow by Life
X-rays and crystals
vte
Electromagnetic spectrum
vte
Nuclear technology
vte
Radiation (physics and health)
Authority control Edit this at Wikidata	
GND: 4129728-3LCCN: sh85148749NARA: 10645918NDL: 00561905
Categories: X-raysElectromagnetic spectrumIARC Group 1 carcinogensIonizing radiationMedical physicsRadiographyWilhelm Röntgen1895 in science1895 in Germany
Navigation menu
Not logged inTalkContributionsCreate accountLog inArticleTalkReadEditView historySearch
Search Wikipedia
Main page
Contents
Featured content
Current events
Random article
Donate to Wikipedia
Wikipedia store
Interaction
Help
About Wikipedia
Community portal
Recent changes
Contact page
Tools
What links here
Related changes
Upload file
Special pages
Permanent link
Page information
Wikidata item
Cite this page
In other projects
Wikimedia Commons
Print/export
Download as PDF
Printable version

Languages
Deutsch
Español
Français
한국어
हिन्दी
Italiano
Tagalog
Tiếng Việt
中文
103 more
Edit links
This page was last edited on 2 March 2020, at 10:09 (UTC).
Text is available under the Creative Commons Attribution-ShareAlike License; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. Wikipedia® is a registered trademark of the Wikimedia Foundation, Inc., a non-profit organization."""
s="""List of civilian nuclear accidents
From Wikipedia, the free encyclopedia
Jump to navigationJump to search
See also: Lists of nuclear disasters and radioactive incidents
This article lists notable civilian accidents involving fissile nuclear material or nuclear reactors. Military accidents are listed at List of military nuclear accidents. Civil radiation accidents not involving fissile material are listed at List of civilian radiation accidents. For a general discussion of both civilian and military accidents, see Nuclear and radiation accidents.


Contents
1	Scope of this article
2	1950s
3	1960s
4	1970s
5	1980s
6	1990s
7	2000s
8	2010s
9	See also
10	References
11	External links
Scope of this article
In listing civilian nuclear accidents, the following criteria have been followed:

Notably severe: there must be well-attested and substantial health damage, property damage or contamination; if an International Nuclear Event Scale (INES) level is available, of at least two.
Nuclear aspect: the damage must be related directly to nuclear operations or materials; the event should involve fissile material or a reactor, not merely (for example) having occurred at the site of a nuclear power plant.
Primarily civilian: the nuclear operation/material must be principally for non-military purposes.
1950s
12 December 1952 — INES Level 5[1] – Chalk River, Ontario, Canada – Reactor core damaged
A reactor shutoff rod failure, combined with several operator errors, led to a major power excursion of more than double the reactor's rated output at AECL's NRX reactor. The operators purged the reactor's heavy water moderator, and the reaction stopped in under 30 seconds. A subsequent cover gas system failure led to hydrogen explosions, which severely damaged the reactor core. The fission products from approximately 30 kg (66 lb) of uranium were released through the reactor stack. Contaminated light water coolant leaked from the damaged coolant circuit into the reactor building; some 4,000 m3 (140,000 cu ft) were pumped via pipeline to a disposal area to avoid contamination of the Ottawa River. Subsequent monitoring of surrounding water sources revealed no contamination. After the incident, approximately 1202 people were involved in the two-year-long cleanup.[2] No immediate fatalities or injuries resulted from the incident; a 1982 follow-up study of exposed workers showed no long-term health effects, though Atomic Energy of Canada Limited (AECL) dosimetry files were lost in a 1956 fire. Future U.S. President Jimmy Carter, a nuclear engineer and then a lieutenant in the U.S. Navy, was among the cleanup crew.[3]
29 Sept 1957 — INES Level 6 — Mayak plutonium-production plant — Nuclear waste tank explosion — Main Article: Kyshtym disaster
10 Oct 1957 — INES Level 5 — Windscale, plutonium production reactor
In the Windscale fire, the reactor core caught fire leading to radioactive materials released across UK and Europe.
24 May 1958 — INES Level needed – Chalk River, Ontario, Canada – Fuel damaged
Due to inadequate cooling, a damaged uranium fuel rod caught fire and was torn in two as it was being removed from the core at the NRU reactor. The fire was extinguished, but not before radioactive combustion products contaminated the interior of the reactor building and, to a lesser degree, an area surrounding the laboratory site. Approximately 679 people were employed in the clean-up.[4][5] A corporal named Bjarnie Hannibal Paulson who was at the cleanup did not die from his exposure, but developed unusual skin cancers. Paulson had to testify at many hearings before he was awarded compensation for his radiation injuries.[6]
25 October 1958 — INES Level needed – Vinča, Serbia (then Yugoslavia) – Criticality excursion, irradiation of personnel
During a subcritical counting experiment, a power buildup went undetected at the Vinca Nuclear Institute's zero-power natural uranium heavy water-moderated research reactor.[7] Saturation of radiation detection chambers gave the researchers false readings and the level of moderator in the reactor tank was raised, triggering a power excursion which a researcher detected from the smell of ozone.[8] Six scientists received radiation doses of 2–4 sieverts (200–400 rem) [9] (p. 96). An experimental bone marrow transplant treatment was performed on all of them in France and five survived, despite the ultimate rejection of the marrow in all cases. A single woman among them later had a child without apparent complications. This was one of the first nuclear incidents investigated by then-newly formed IAEA.[10]
26 July 1959 — INES Level needed – Santa Susana Field Laboratory, California, United States – Partial meltdown
A partial core meltdown took place when the Sodium Reactor Experiment (SRE) experienced a power excursion that caused severe overheating of the reactor core, resulting in the melting of one-third of the nuclear fuel and significant release of radioactive gases. The amount of radioactivity released is disputed, with it ranging from 28 Curies [11] to as much as 240 to 260 times worse than Three Mile Island. Over the succeeding years, the site was cleaned up and all buildings and contamination removed. The soil was removed and other soil[12] brought in and now forms a portion of an area near the Simi Valley Adventist Hospital.[13]
1960s
3 April 1960 — INES Level needed – Westmoreland County, Pennsylvania, United States – Core melt accident
A core meltdown occurred at the Westinghouse Waltz Mill test reactor. From what information remains of the event, one fuel element melted, resulting in the disposition of 2 million gallons of contaminated water generated during the accident. At least a portion of the water was retained on site in lagoons, a condition which eventually led to detectable 90Sr in groundwater plus contaminated soil. The site is currently undergoing cleanup.
24 July 1964 — INES Level needed – Wood River Junction, Richmond, Rhode Island, United States – Criticality accident
A worker at a United Nuclear Corporation fuel facility led to an accidental criticality. Robert Peabody, believing he was using a diluted uranium solution, accidentally put concentrated solution into an agitation tank containing sodium carbonate. Peabody was exposed to 100 Gy (10,000 rad) of radiation and died two days later. Ninety minutes after the criticality, a plant manager and another administrator returned to the building and were exposed to 1 Gy (100 rad), but suffered no ill effects.[14][15]
5 October 1966 — INES Level 4 – Monroe, Michigan, United States – Partial meltdown
A sodium cooling system malfunction caused the meltdown of some fuel elements at the Fermi 1 fast breeder reactor. The accident was attributed to a zirconium fragment that obstructed a flow-guide in the sodium cooling system. Two of the 105 fuel assemblies melted during the accident, but no contamination was recorded outside the containment vessel.[16]
Winter 1966-1967 (date unknown) — INES Level needed – location unknown – Loss of coolant accident
The Soviet Navy icebreaker Lenin, the USSR’s first nuclear-powered surface ship, suffered a major accident (possibly a nuclear meltdown — exactly what happened remains a matter of controversy in the West) in one of its three reactors. To find the leak the crew broke through the concrete and steel radiation shield with sledgehammers, causing irreparable damage. It was rumored that around 30 of the crew were killed. The ship was abandoned for a year to allow radiation levels to drop before the three reactors were removed, to be dumped into the Tsivolko Fjord on the Kara Sea, along with 60% of the fuel elements packed in a separate container. The reactors were replaced with two new ones, and the ship reentered service in 1970, serving until 1989.
May 1967 — INES Level needed – Dumfries and Galloway, Scotland, United Kingdom – Partial meltdown
Graphite debris partially blocked a fuel channel causing a fuel element to melt and catch fire at the Chapelcross nuclear power station. Contamination was confined to the reactor core. The core was repaired and restarted in 1969, operating until the plant's shutdown in 2004.[17][18]
21 January 1969 — INES Level 4 – Lucens, Canton of Vaud, Switzerland – Explosion
A total loss of coolant led to a power excursion and explosion of the Lucens reactor, an experimental reactor in a large rock cavern at Lucens. The underground location of this reactor acted like a containment building and prevented any outside contamination. The cavern was contaminated and was sealed. No injuries or fatalities resulted.[19][20]
Defueling and partial dismantling occurred from 1969 to 1973. In 1988, the lowest caverns were filled with concrete, and a regulatory permit was issued in December 1990. Currently, the archives of the Canton of Vaud are located in the caverns.[21]
1970s
7 December 1975 — INES Level 3 – Greifswald, Germany (then East Germany) – Station blackout
A fire in a cable duct after a short circuit disabled the electrical power supply for all feedwater and emergency core cooling pumps. A power supply was improvised by the operating personnel after several hours.
22 February 1977 — INES Level 4 – Jaslovské Bohunice, Slovakia (then Czechoslovakia) – Fuel damaged
Operators neglected to remove moisture-absorbing materials from a fuel rod assembly before loading it into the KS 150 reactor at power plant A-1. The accident resulted in damaged fuel integrity, extensive corrosion damage of fuel cladding and release of radioactivity into the plant area. The affected reactor was decommissioned following this accident.[22]
28 March 1979 — INES Level 5[1] – Middletown, Dauphin County, Pennsylvania, United States – Partial meltdown
Equipment failures, poor user interface design, and worker mistakes contributed to a loss of coolant and a partial core meltdown at the Three Mile Island Nuclear Generating Station 15 km (9.3 mi) southeast of Harrisburg. While the reactor was extensively damaged, on-site radiation exposure was under 100 millirems (less than annual exposure due to natural sources). Area residents received a smaller exposure of 1 millirem (10 μSv), or about 1/3 the dose from eating a banana per day for one year. There were no fatalities. Follow-up radiological studies predict between zero and one long-term cancer fatality.[23][24][25]
1980s
13 March 1980 — INES Level 4 – Saint-Laurent-des-Eaux, France – Nuclear materials leak
A brief power excursion in Reactor A2 led to a rupture of fuel bundles and a minor 80 GBq (2,200 mCi) release of nuclear materials at the Saint-Laurent Nuclear Power Plant. The reactor was repaired and continued operation until its decommissioning in 1992.[26]
March 1981 — INES Level 2 – Tsuruga, Japan – Radioactive materials released into Sea of Japan; overexposure of workers
More than 100 workers were exposed to doses of up to 1.55 mSv (155 mrem) per day radiation during repairs of the Tsuruga Nuclear Power Plant, violating the Japan Atomic Power Company's limit of 1 mSv (100 mrem) per day.[27]
23 September 1983 — INES Level 4 – Buenos Aires, Argentina – Accidental criticality
An operator error during a fuel plate reconfiguration in an experimental test reactor led to an excursion of 3×1017 fissions at the RA-2 facility. The operator absorbed 20 Gy of gamma and 17 Gy of neutron radiation which killed him two days later. Another 17 people outside of the reactor room absorbed doses ranging from 350 mGy to less than 10 mGy.[28] pg103[29]
26 April 1986 — INES Level 7 – Pripyat, Ukraine (then Ukrainian Soviet Socialist Republic, Union of Soviet Socialist Republics) – Power excursion, explosion, complete meltdown
An inadequate reactor safety system test[30] led to an uncontrolled power excursion, causing a severe steam explosion, meltdown, and release of radioactive materials at the Chernobyl nuclear power plant located approximately 100 kilometers (60 miles) north-northwest of Kiev. Approximately 50 fatalities (mostly cleanup personnel) resulted from the accident and the immediate aftermath. An additional nine fatal cases of thyroid cancer in children in the Chernobyl area have been attributed to the accident. The explosion and combustion of the graphite reactor core spread radioactive material over much of Europe. 100,000 people were evacuated from the areas immediately surrounding Chernobyl in addition to 300,000 from the areas of heavy fallout in Ukraine, Belarus and Russia. An "Exclusion Zone" was created surrounding the site encompassing approximately 3,000 km2 (1,200 sq mi) and deemed off-limits for human habitation for an indefinite period. Several studies by governments, U.N. agencies and environmental groups have estimated the consequences and eventual number of casualties. Their findings are subject to controversy.
4 May 1986 — no INES Level – Hamm-Uentrop, Germany (then West Germany) – Fuel damaged
Spherical fuel pebbles became lodged in the pipe used to deliver fuel elements to the reactor at an experimental 300-megawatt THTR-300 HTGR. Attempts by an operator to dislodge the fuel pebble damaged the pipe, releasing activated coolant gas which was detectable up to two kilometers from the reactor.[31]
1990s
6 April 1993 — INES Level 4 – Tomsk, Russia – Explosion
A pressure buildup led to an explosive mechanical failure in a 34 m3 (1,200 cu ft) stainless steel reaction vessel buried in a concrete bunker under building 201 of the radiochemical works at the Tomsk-7 Siberian Chemical Enterprise plutonium reprocessing facility. The vessel contained a mixture of concentrated nitric acid, 8,757 kg (19,306 lb) uranium, 449 g (15.8 oz) plutonium along with a mixture of radioactive and organic waste from a prior extraction cycle. The explosion dislodged the concrete lid of the bunker and blew a large hole in the roof of the building, releasing approximately 6 GBq (160 mCi) of Pu 239 and 30 TBq (810 Ci) of other radionuclides into the environment. The contamination plume extended 28 km (17 mi) NE of building 201, 20 km (12 mi) beyond the facility property. The small village of Georgievka (pop. 200) was at the end of the fallout plume, but no fatalities, illnesses or injuries were reported. The accident exposed 160 on-site workers and almost two thousand cleanup workers to total doses of up to 50 mSv (the threshold limit for radiation workers is 20 mSv/yr).[32][33][34]
June 1999 — INES Level 2[35] – Ishikawa Prefecture, Japan – Control rod malfunction
Operators attempting to insert one control rod during an inspection neglected procedure and instead withdrew three causing a 15 minute uncontrolled sustained reaction at the number 1 reactor of Shika Nuclear Power Plant. The Hokuriku Electric Power Company who owned the reactor did not report this incident and falsified records, covering it up until March, 2007.[36]
30 September 1999 — INES Level 4 – Ibaraki Prefecture, Japan – Accidental criticality
Inadequately trained part-time workers prepared a uranyl nitrate solution containing about 16.6 kg (37 lb) of uranium, which exceeded the critical mass, into a precipitation tank at a uranium reprocessing facility in Tokai-mura northeast of Tokyo, Japan. The tank was not designed to dissolve this type of solution and was not configured to prevent eventual criticality. Three workers were exposed to (neutron) radiation doses in excess of allowable limits. Two of these workers died. 116 other workers received lesser doses of 1 mSv or greater though not in excess of the allowable limit.[37][38][39][40]
2000s
10 April 2003 — INES Level 3 – Paks, Hungary – Fuel damaged
Partially spent fuel rods undergoing cleaning in a tank of heavy water ruptured and spilled fuel pellets at Paks Nuclear Power Plant. It is suspected that inadequate cooling of the rods during the cleaning process combined with a sudden influx of cold water thermally shocked fuel rods causing them to split. Boric acid was added to the tank to prevent the loose fuel pellets from achieving criticality. Ammonia and hydrazine were also added to absorb 131I.[41]
19 April 2005 — INES Level 3 – Sellafield, England, United Kingdom – Nuclear material leak
20 t (20 long tons; 22 short tons) of uranium and 160 kg (350 lb) of plutonium dissolved in 83 kl (2,900 cu ft) of nitric acid leaked over several months from a cracked pipe into a stainless steel sump chamber at the Thorp nuclear fuel reprocessing plant. The partially processed spent fuel was drained into holding tanks outside the plant.[42][43]
November 2005 — INES Level needed – Braidwood, Illinois, United States – Nuclear material leak
Tritium contamination of groundwater was discovered at Exelon's Braidwood station. Groundwater off site remains within safe drinking standards though the NRC is requiring the plant to correct any problems related to the release.[44]
6 March 2006 — INES Level 2[45] – Erwin, Tennessee, United States – Nuclear material leak
35 l (7.7 imp gal; 9.2 US gal) of a highly enriched uranium solution leaked during transfer into a lab at Nuclear Fuel Services Erwin Plant. The incident caused a seven-month shutdown. A required public hearing on the licensing of the plant was not held due to the absence of public notification.[46][47][48][49]
4 May 2009 — INES Level 2[50] – Paks, Hungary – A device fallen in the reactor hall while transported.[51][52][53]
2010s
11–20 March 2011 — INES Level 7[54][55] Fukushima Daiichi ("Fukushima I") Nuclear Power Plant, Japan – Partial meltdowns in multiple reactors[56]
(The INES 7 rating is as of April 12, 2011. The previous INES rating had been 5,[57] a final rating is expected after the situation has been completely resolved)
After the 2011 Tōhoku earthquake and tsunami of March 11, the emergency power supply of the Fukushima-Daiichi nuclear power plant failed. This was followed by deliberate releases of radioactive gas from reactors 1 and 2 to relieve pressure.
March 12: triggered by falling water levels and exposed fuel rods, a hydrogen explosion occurred at reactor 1, resulting in the collapse of the concrete outer structure.[58][59][60][61][62] Although the reactor containment itself was confirmed to be intact,[63][64][65] the hourly radiation from the plant reached 1.015 mSv (0.1015 rem) - an amount equivalent to that allowable for ordinary people in one year.[66][67]
Residents of the Fukushima area were advised to stay inside, close doors and windows, turn off air conditioning, and to cover their mouths with masks, towels or handkerchiefs as well as not to drink tap water.[68] By the evening of March 12, the exclusion zone had been extended to 20 kilometres (12 mi) around the plant[69] and 70,000 to 80,000 people had been evacuated from homes in northern Japan.[70]
March 14: a second, hydrogen explosion (nearly identical to the first explosion in Unit 1) occurred in the reactor building for Unit 3, with similar effects.[71]
March 15: a third explosion occurred in the “pressure suppression room” of Unit 2[72] and is initially said not to have breached the reactor’s inner steel containment vessel,[73] but later reports indicated that the explosion damaged the steel containment structure of Unit 2 and much larger releases of radiation were expected than previously.[72] That same day, a fourth explosion damaged the 4th floor area above the reactor and spent fuel pool of the Unit 4 reactor.[74] Contrary to the TEPCO press release, aerial photos show that most of the outer building was actually destroyed. The fuel rods (both new and spent fuel) of reactor Unit 4, stored in the now exposed spent fuel pool, were reportedly exposed to air – this would have risked the melting of the nuclear fuel. However, later research found the fuel rods had been covered by water all the time.[75][76]
TEPCO estimated that 70% of the fuel in Unit 1 had melted, and 33% in Unit 2, further suspecting that Unit 3's core might also be damaged.[77] In November 2011 TEPCO released the report of the Modular Accident Analysis Program (MAAP).[78] The report showed that the reactor pressure vessel (RPV) in Unit 1 (commonly known as the reactor core) had been damaged during the disaster, and that significant amounts of fuel had fallen into the bottom of the primary containment vessel (PCV) – the erosion of the concrete of the PCV by the molten fuel immediately after the disaster was estimated to have been stopped in approx. 0.7 metres (2 ft 4 in) depth, with the thickness of the containment being 7.6 metres (25 ft). Gas sampling done before the report detected no signs of an ongoing reaction of the fuel with the concrete of the PCV and all the fuel in Unit 1 was estimated to be "well cooled down, including the fuel dropped on the bottom of the reactor". MAAP further showed that fuel in Unit 2 and Unit 3 had melted, however less than Unit 1, and fuel was presumed to be still in the RPV, with no significant amounts of fuel fallen to the bottom of the PCV. The report further suggested that "there is a range in the evaluation results" from "most fuel in the RPV (some fuel in PCV)" in Unit 2 and Unit 3, to "all fuel in the RPV (none fuel fallen to the PCV)". For Unit 2 and Unit 3 it was estimated that the "fuel is cooled sufficiently". The larger damage in Unit 1 was according to the report due to long time that cooling water was not injected in Unit 1, letting much more decay heat accumulate – for about 1 day there was no water injection for Unit 1, while Unit 2 and Unit 3 had only a quarter of a day without water injection. As of December 2013, it was reported that TEPCO estimated for Unit 1 that "the decay heat must have decreased enough, the molten fuel can be assumed to remain in PCV (Primary container vessel)".[79]
See also
Criticality accident
International Nuclear Events Scale
List of Chernobyl-related articles
List of civilian nuclear incidents
List of civilian radiation accidents
List of industrial disasters
List of military nuclear accidents
List of crimes involving radioactive substances
List of nuclear reactors — a comprehensive annotated list of the world's nuclear reactors
Lists of nuclear disasters and radioactive incidents
Nuclear and radiation accidents
Nuclear reactor technology
Nuclear power
Nuclear power debate
Radiation
List of hydroelectric power station failures
References
 International Association for Engineering Geology and the Environment (IAEG). International Congress (2014), Lollino, Giorgio; Arattano, Massimo; Giardino, Marco; Oliveira, Ricardo; Silvia, Peppoloni (eds.), Engineering Geology for Society and Territory: Education, professional ethics and public recognition of engineering geology, Volume 7, Springer, p. 192, ISBN 9783319093031, retrieved 24 November 2014
 "The NRX Incident" by Peter Jedicke
 "The Canadian Nuclear FAQ - Section D: Safety and Liability".
 "Reactor Accidents at Chalk River:The Human Fallout" by Dr. Gordon Edwards
 "What are the details of the accident at Chalk River's NRU reactor in 1958?" by Dr. Jeremy Whitlock
 "The Canadian Coalition for Nuclear Responsibility" letter by Dr. Gordon Edwards
 [1]
 "Vinca reactor accident, 1958".
 "Archived copy" (PDF). Archived from the original (PDF) on 2009-03-20. Retrieved 2008-02-28.
 [2]
 The Boeing Company (March 23, 2006). “The Sodium Reactor Experiment "The Sodium Reactor Experiment" Check |url= value (help). Retrieved 22 April 2012.
 Rockwell International Corporation, Energy Systems Group. "Sodium Reactor Experiment Decommissioning Final Report" (PDF). ESG-DOE-13403. Retrieved 21 May 2014.
 [3]
 http://www.bazley.net/institute/archives/UNCdeath.html
 McLaughlin et al. pages 33-34
 "Nuclear Accidents".
 [4]
 "Archived copy". Archived from the original on 2011-05-20. Retrieved 2011-04-28.
 [5]
 [6]
 "Interface between Operator, Regulatory Body and Public" at IAEA.org
 "Archived copy". Archived from the original on 2007-11-21. Retrieved 2007-04-01.
 [7]
 [8]
 [9]
 [10]
 [11]
 [12]
 [13]
 (memoires of vice chief engineer of operation Anatoly Dyatlov, in Russian)
 [Begründung zur atomrechtlichen Anordnung vom 3. Juni 1986 des Ministers für Wirtschaft, Mittelstand und Technologie, declaration given in the Landtag (parliament) of the state Northrhine-Westphalia on 4th June 1986]
 [14]
 [15]
 Timeline: Nuclear plant accidents
 http://www.climatesceptics.org/event/841
 Japanese utility to shut reactor after admitting accident cover-up
 Tokaimura Criticality Accident
 Tokaimura Criticality Accident Nuclear Issues Briefing Paper #52
 Chronology and Press Reports of the Tokaimura Criticality
 Timeline: Nuclear plant accidents
 Incremented radioactivity of the heat carrier during refueling outage at a time of fuel cleaning | Nuclear power in Europe
 Huge radioactive leak closes Thorp nuclear plant
 British Nuclear Group releases report on Sellafield leak Archived 2007-03-12 at the Wayback Machine
 Exelon Braidwood Nuclear Facility Update on Tritium Releases and Groundwater Impacts
 http://www.climatesceptics.org/event/805
 Federal Register: May 4, 2007 (Volume 72, Number 86)
 Secrecy Shrouds Accident at Nuclear Plant
 More revelations about Nuclear Fuel Services, Inc.
 Erwin nuke problems known
 http://www.climatesceptics.org/event/805
 Belgium, Central Office, NucNet a s b l , Brussels. "Outage Incident At Hungary's Paks-4 Rated INES Level 2". The Independent Global Nuclear News Agency. Retrieved 2019-06-26.
 "Lapok/SajtokozlemenyReszletek.aspx". www.atomeromu.hu (in Hungarian). Retrieved 2019-06-26.
 MTI, Index (2009-05-05). "Üzemzavar a paksi atomerőműben". index.hu (in Hungarian). Retrieved 2019-06-26.
 YURI KAGEYAMA; RYAN NAKASHIMA (April 12, 2011). "Japan ups nuke crisis severity to match Chernobyl". Associated Press. Retrieved April 12, 2011.
 "IAEA Briefing on Fukushima Nuclear Accident (12 April 2011, 14:30 UTC)". April 12, 2011.
 "Tepco confirms extra partial fuel rod meltdown at plant". BBC News. May 24, 2011.
 "Nuclear accident rated at level 4". NHK World. Archived from the original on March 13, 2011. Retrieved March 12, 2011.
 "福島第一原発爆発の瞬間 nuclear power station explosion Fukushima Japan". YouTube. Retrieved March 12, 2011.
 Fox News Channel Breaking News Alert (live TV coverage), 3:00 am EST, March 12
 Live blog, BBC News, March 12, 2011
 Fredrik Dahl; Louise Ireland (March 12, 2011). "Hydrogen may have caused Japan atom blast-industry". Reuters. Retrieved March 12, 2011.
 "Explosion heard at quake-hit reactor". NHK World. March 12, 2011.
 World Nuclear News (March 12, 2011). "Battle to stabilise earthquake reactors". World Nuclear News. Retrieved March 12, 2011.
 "Japan to fill leaking nuke reactor with sea water". Reuters. March 12, 2011.
 Explosion at Fukushima I reactor 1; 4 injured, 3 irradiated (Japanese)
 "Explosion at quake-hit nuclear plant". ABC News (Australian Broadcasting Corporation). March 12, 2011. Retrieved March 12, 2011.
 See also: "Radiation dose limits". Bbc.co.uk. Retrieved March 12, 2011.
 Glendinning, Lee (March 12, 2011). "Japan tsunami and earthquake - live coverage | World news | guardian.co.uk". London: Guardian. Retrieved March 12, 2011.
 "Japan earthquake | Page 18 | Liveblog live blogging | Reuters.com". Live.reuters.com. February 9, 2009. Retrieved March 12, 2011.
 NHK News 7 (TV coverage), March 13, 2011, 10:46 UTC
 "Blast, cooling system breakdown spread fears of nuclear radiation". CNN. March 14, 2011.
 Hiroko Tabuchi; Keith Bradsher; Matt Wald (March 14, 2011). "Japan Faces Prospect of Nuclear Catastrophe as Workers Leave Plant". The New York Times.
 "Plant operator says reactor seal apparently not holed". channelnewsasia.com. March 15, 2011.
 "Damage to the Unit 4 Nuclear Reactor Building at Fukushima Dai-ichi Nuclear Power Station" (Press release). Tokyo Electric Power Company. 15 March 2011. Retrieved 26 February 2013.
 Hiroko Tabuchi, Keith Bradsher,David E. Sanger Matthew L. Wald (March 15, 2011). "Fire and Damage at Japanese Plant Raise Risk of Nuclear Disaster". The New York Times.
 http://www.tepco.co.jp/en/nu/fukushima-np/images/handouts_120516_07-e.pdf
 Fukushima Timeline scientificamerican.com
 The Evaluation Status of Reactor Core Damage at Fukushima Daiichi Nuclear Power Station Units 1 to 3 November 30, 2011 Tokyo Electric Power Company
 Most of fuel NOT remaining in reactor1 core / Tepco “but molten fuel is stopped in the concrete base” Fukushima-Diary.com
External links
Nuclear power plant accidents: listed and ranked since 1952
Timeline: Nuclear plant accidents
ProgettoHumus - Mondo in Cammino: List updated of nuclear accidents in the history
Schema-root.org: Nuclear Power Accidents 2 topics, both with a current news feed
US Nuclear Regulatory Commission (NRC) website with search function and electronic public reading room
International Atomic Energy Agency website with extensive online library
Canada's Nuclear Safety Commission (CNSC)
Concerned Citizens for Nuclear Safety Detailed articles on nuclear watchdog activities in the US
World Nuclear Association: Radiation Doses Background on ionizing radiation and doses
Canadian Centre for Occupational Health & Safety More information on radiation units and doses.
Radiological Incidents Database Extensive, well-referenced list of radiological incidents.
Critical Hour: Three Mile Island, The Nuclear Legacy, And National Security Online book by Albert J. Fritsch, Arthur H. Purcell, and Mary Byrd Davis
Annotated bibliography on civilian nuclear accidents from the Alsos Digital Library for Nuclear Issues.
Partial list of Indian nuclear accidents
vte
Lists of nuclear disasters and radioactive incidents
vte
Disasters
Overview	
Lists by death tollby cost
Disasters	
vte
Natural disasters · list by death toll
Anthropogenics	
Accidents	
Transport	
RailMaritimeShipwreckAirSpaceflight
Industrial	
Structural failures and collapsesBridgeDamNuclear by death tollCivilian radiationCivilian nuclearMilitary nuclearOil spillsLevee breachMast and towerInfrastructure
Health	
Famine ListFamine scalesEpidemic listPandemic
Man-made	
Wars and anthropogenic disastersBattles and other violent eventsMilitaryWarsTerrorist incidentsRiotsMassacresNightclub fires
Countermeasures	
Humanitarian aidEmergency population warningEmergency Alert SystemEarthquake preparednessEarthquake warning systemEvacuationsEmergency managementHurricane preparednessHurricane responseCrisis managementDisaster risk reduction
Media	
Disaster film (List of disaster films)
Organizations	
International Association of Emergency ManagersInternational Disaster and Risk ConferenceDisaster Accountability ProjectInternational Disaster Emergency Service
WikiProject WikiProject
Radioactive.svgNuclear technology portal
Categories: Civilian nuclear power accidentsNuclear safety and securityLists of nuclear disastersNuclear technology-related lists
Navigation menu
Not logged inTalkContributionsCreate accountLog inArticleTalkReadEditView historySearch
Search Wikipedia
Main page
Contents
Featured content
Current events
Random article
Donate to Wikipedia
Wikipedia store
Interaction
Help
About Wikipedia
Community portal
Recent changes
Contact page
Tools
What links here
Related changes
Upload file
Special pages
Permanent link
Page information
Wikidata item
Cite this page
Print/export
Download as PDF
Printable version

Languages
Čeština
Deutsch
Español
Français
日本語
Русский
Svenska
3 more
Edit links
This page was last edited on 24 February 2020, at 11:44 (UTC).
Text is available under the Creative Commons Attribution-ShareAlike License; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. Wikipedia® is a registered trademark of the Wikimedia Foundation, Inc., a non-profit organization."""

s="http://en.wikipedia.org/wiki/Lists_of_accnuclear"
p=get_relevance_count(s)
print(p)

s="""
Control rod
From Wikipedia, the free encyclopedia
Jump to navigationJump to search

Control rod assembly for a pressurized water reactor, above fuel element
Control rods are used in nuclear reactors to control the fission rate of uranium or plutonium. Their compositions includes chemical elements such as boron, cadmium, silver, or indium, that are capable of absorbing many neutrons without themselves fissioning. These elements have different neutron capture cross sections for neutrons of various energies. Boiling water reactors (BWR), pressurized water reactors (PWR), and heavy-water reactors (HWR) operate with thermal neutrons, while breeder reactors operate with fast neutrons. Each reactor design can use different control rod materials based on the energy spectrum of its neutrons.


Contents
1	Operating principle
2	Materials
2.1	Additional means of reactivity regulation
3	Safety
3.1	Criticality accident prevention
4	See also
5	References
6	External links
7	Further reading
Operating principle

1943 Reactor diagram using boron control rods
Control rods are inserted into the core of a nuclear reactor and adjusted in order to control the rate of the nuclear chain reaction and, thereby, the thermal power output of the reactor, the rate of steam production, and the electrical power output of the power station.

The number of control rods inserted, and the distance to which they are inserted, strongly influence the reactivity of the reactor. When reactivity (as effective neutron multiplication factor) is above 1, the rate of the nuclear chain reaction increases exponentially over time. When reactivity is below 1, the rate of the reaction decreases exponentially over time. When all control rods are fully inserted, they keep reactivity barely above 0, which quickly slows a running reactor to a stop and keeps it stopped (in shutdown). If all control rods are fully removed, reactivity is significantly above 1, and the reactor quickly runs hotter and hotter, until some other factor slows the reaction rate. Maintaining a constant power output requires keeping the long-term average neutron multiplication factor close to 1.

A new reactor is assembled with its control rods fully inserted. Control rods are partially removed from the core to allow the nuclear chain reaction to start up and increase to the desired power level. Neutron flux can be measured, and is roughly proportional to reaction rate and power level. To increase power output, some control rods are pulled out a small distance for a while. To decrease power output, some control rods are pushed in a small distance for a while. Several other factors affect the reactivity; to compensate for them, an automatic control system adjusts the control rods small amounts in or out, as-needed. Each control rod influences some part of the reactor more than others; complex adjustments can be made to maintain similar reaction rates and temperatures in different parts of the core.

Typical shutdown time for modern reactors such as the European Pressurized Reactor or Advanced CANDU reactor is 2 seconds for 90% reduction, limited by decay heat.

Control rods are usually used in control rod assemblies (typically 20 rods for a commercial PWR assembly) and inserted into guide tubes within the fuel elements. Control rods often stand vertically within the core. In PWRs they are inserted from above, with the control rod drive mechanisms mounted on the reactor pressure vessel head. In BWRs, due to the necessity of a steam dryer above the core, this design requires insertion of the control rods from beneath.

Materials

The absorption cross section for 10B (top) and 11B (bottom) as a function of energy
Chemical elements with usefully high neutron capture cross-sections include silver, indium, and cadmium. Other candidate elements include boron, cobalt, hafnium, samarium, europium, gadolinium, terbium, dysprosium, holmium, erbium, thulium, ytterbium, and lutetium.[1] Alloys or compounds may also be used, such as high-boron steel,[2] silver-indium-cadmium alloy, boron carbide, zirconium diboride, titanium diboride, hafnium diboride, gadolinium nitrate,[3] gadolinium titanate, dysprosium titanate, and boron carbide–europium hexaboride composite.[4]

The material choice is influenced by the neutron energy in the reactor, their resistance to neutron-induced swelling, and the required mechanical and lifespan properties. The rods may have the form of tubes filled with neutron-absorbing pellets or powder. The tubes can be made of stainless steel or other "neutron window" materials such as zirconium, chromium, silicon carbide, or cubic 11
B15
N (cubic boron nitride).[5]

The burnup of "burnable poison" isotopes also limits lifespan of a control rod. They may be reduced by using an element such as hafnium, a "non-burnable poison" which captures multiple neutrons before losing effectiveness, or by not using neutron absorbers for trimming. For example, in pebble bed reactors or in possible new type lithium-7-moderated and -cooled reactors that use fuel and absorber pebbles.

Some rare-earth elements are excellent neutron absorbers and are less rare than silver (reserves of about 500,000t). For example, ytterbium (reserves about 1 M tons) and yttrium, 400 times more common, with middle capturing values, can be found and used together without separation inside minerals like xenotime (Yb) (Yb0.40Y0.27Lu0.12Er0.12Dy0.05Tm0.04Ho0.01)PO4,[6] or keiviite (Yb) (Yb1.43Lu0.23Er0.17Tm0.08Y0.05Dy0.03Ho0.02)2Si2O7, lowering the cost.[7] Xenon is also a strong neutron absorber as a gas, and can be used for controlling and (emergency) stopping helium-cooled reactors, but does not function in cases of pressure loss, or as a burning protection gas together with argon around the vessel part especially in case of core catching reactors or if filled with sodium or lithium. Fission-produced xenon can be used after waiting for caesium to precipitate, when practically no radioactivity is left. Cobalt-59 is also used as an absorber for winning of cobalt-60 for X-ray production. Control rods can also be constructed as thick turnable rods with a tungsten reflector and absorber side turned to stop by a spring in less than 1 second.

Silver-indium-cadmium alloys, generally 80% Ag, 15% In, and 5% Cd, are a common control rod material for pressurized water reactors.[8] The somewhat different energy absorption regions of the materials make the alloy an excellent neutron absorber. It has good mechanical strength and can be easily fabricated. It must be encased in stainless steel to prevent corrosion in hot water.[9] Although indium is less rare than silver, it is more expensive.

Boron is another common neutron absorber. Due to the different cross sections of 10B and 11B, materials containing boron enriched in 10B by isotopic separation are frequently used. The wide absorption spectrum of boron also makes it suitable as a neutron shield. The mechanical properties of boron in its elementary form are unsuitable, and therefore alloys or compounds have to be used instead. Common choices are high-boron steel and boron carbide. The latter is used as a control rod material in both PWRs and BWRs. 10B/11B separation is done commercially with gas centrifuges over BF3, but can also be done over BH3 from borane production or directly with an energy optimized melting centrifuge, using the heat of freshly separated boron for preheating.

Hafnium has excellent properties for reactors using water for both moderation and cooling. It has good mechanical strength, can be easily fabricated, and is resistant to corrosion in hot water.[10] Hafnium can be alloyed with other elements, e.g. with tin and oxygen to increase tensile and creep strength, with iron, chromium, and niobium for corrosion resistance, and with molybdenum for wear resistance, hardness, and machineability. Such alloys are designated as Hafaloy, Hafaloy-M, Hafaloy-N, and Hafaloy-NM.[11] The high cost and low availability of hafnium limit its use in civilian reactors, although it is used in some US Navy reactors. Hafnium carbide can also be used as an insoluble material with a high melting point of 3890 °C and density higher than that of uranium dioxide for sinking, unmelted, through corium.

Dysprosium titanate was undergoing evaluation for pressurized water control rods. Dysprosium titanate is a promising replacement for Ag-In-Cd alloys because it has a much higher melting point, does not tend to react with cladding materials, is easy to produce, does not produce radioactive waste, does not swell and does not outgas. It was developed in Russia and is recommended by some for VVER and RBMK reactors.[12] A disadvantage is less titanium and oxide absorption, that other neutron absorbing elements do not react with the already high-melting point cladding materials and that just using the unseparated content with dysprosium inside of minerals like Keiviit Yb inside chromium, SiC or c11B15N tubes deliver superior price and absorption without swelling and outgassing.

Hafnium diboride is another such material. It can be used alone or in a sintered mixture of hafnium and boron carbide powders.[13]

Many other compounds of rare-earth elements can be used, such as samarium with boron-like europium and samarium boride, which is already used in the colour industry.[14] Less absorptive compounds of boron similar to titanium, but inexpensive, such as molybdenum as Mo2B5. Since they all swell with boron, in practice other compounds are better, such as carbides, etc., or compounds with two or more neutron-absorbing elements together. It is important that tungsten, and probably also other elements like tantalum,[15] have much the same high capture qualities as hafnium,[16] but with the opposite effect. This is not explainable by neutron reflection alone. An obvious explanation is resonance gamma rays increasing the fission and breeding ratio versus causing more capture of uranium, etc. over metastable conditions like for isotope 235mU, which has a half-life of about 26 min.

Additional means of reactivity regulation
Other means of controlling reactivity include (for PWR) a soluble neutron absorber (boric acid) added to the reactor coolant, allowing the complete extraction of the control rods during stationary power operation, ensuring an even power and flux distribution over the entire core. This chemical shim, along with the use of burnable neutron poisons within the fuel pellets, is used to assist regulation of the core's long term reactivity,[17] while the control rods are used for rapid reactor power changes (e.g. shutdown and start up). Operators of BWRs use the coolant flow through the core to control reactivity by varying the speed of the reactor recirculation pumps (an increase in coolant flow through the core improves the removal of steam bubbles, thus increasing the density of the coolant/moderator, increasing power).

Safety
In most reactor designs, as a safety measure, control rods are attached to the lifting machinery by electromagnets, rather than direct mechanical linkage. This means that in the event of power failure, or if manually invoked due to failure of the lifting machinery, the control rods fall automatically, under gravity, all the way into the pile to stop the reaction. A notable exception to this fail-safe mode of operation is the BWR, which requires hydraulic insertion in the event of an emergency shut-down, using water from a special tank under high pressure. Quickly shutting down a reactor in this way is called scramming.

Criticality accident prevention
Mismanagement or control rod failure have often been blamed for nuclear accidents, including the SL-1 explosion and the Chernobyl disaster. Homogeneous neutron absorbers have often been used to manage criticality accidents which involve aqueous solutions of fissile metals. In several such accidents, either borax (sodium borate) or a cadmium compound has been added to the system. The cadmium can be added as a metal to nitric acid solutions of fissile material; the corrosion of the cadmium in the acid will then generate cadmium nitrate in situ.

In carbon dioxide-cooled reactors such as the AGR, if the solid control rods fail to arrest the nuclear reaction, nitrogen gas can be injected into the primary coolant cycle. This is because nitrogen has a larger absorption cross-section for neutrons than carbon or oxygen; hence, the core then becomes less reactive.

As the neutron energy increases, the neutron cross section of most isotopes decreases. The boron isotope 10B is responsible for the majority of the neutron absorption. Boron-containing materials can also be used as neutron shielding, to reduce the activation of material close to a reactor core.

See also
Nuclear power
Nuclear reactor
Nuclear safety
Wigner effect
References
 ytterbium (n.gamma) data with Japanese or Russian database
 limited to use only in research reactors due to increased swelling from helium and lithium due to neutron absorption of boron in the (n, alpha) reaction
 injected into D2O moderator of Advanced CANDU reactor
 Sairam K, Vishwanadh B, Sonber JK, et al. Competition between densification and microstructure development during spark plasma sintering of B4C–Eu2O3. J Am Ceram Soc. 2017;00:1–11. https://doi.org/10.1111/jace.15376
 Anthony Monterrosa; Anagha Iyengar; Alan Huynh; Chanddeep Madaan (2012). "Boron Use and Control in PWRs and FHRs" (PDF).
 Harvey M. Buck, Mark A. Cooper, Petr Cerny, Joel D. Grice, Frank C. Hawthorne: Xenotime-(Yb), YbPO4,a new mineral species from the Shatford Lake pegmatite group, southeastern Manitoba, Canada. In: Canadian Mineralogist. 1999, 37, S. 1303–1306 (Abstract in American Mineralogist, S. 1324; PDF
 A. V. Voloshin, Ya. A. Pakhomovsky, F. N. Tyusheva: Keiviite Yb2Si2O7, A new ytterbium silicate from amazonitic pegmatites of the Kola Peninsula. In: Mineralog. Zhurnal. 1983, 5-5, S. 94–99 (Abstract in American Mineralogist, S. 1191; PDF; 853 kB).
 Bowsher, B. R.; Jenkins, R. A.; Nichols, A. L.; Rowe, N. A.; Simpson, J. a. H. (1986-01-01). "Silver-indium-cadmium control rod behaviour during a severe reactor accident". UKAEA Atomic Energy Establishment.
 "CONTROL MATERIALS". web.mit.edu. Retrieved 2015-06-02.
 "Control Materials". Web.mit.edu. Retrieved 2010-08-14.
 "Hafnium alloys as neutron absorbers". Free Patents Online. Archived from the original on October 12, 2008. Retrieved September 25, 2008.
 "Dysprosium (Z=66)". Everything-Science.com web forum. Retrieved September 25, 2008.
 "Method for making neutron absorber material". Free Patents Online. Retrieved September 25, 2008.
 "Infrarotabsorbierende Druckfarben - Dokument DE102008049595A1". Patent-de.com. 2008-09-30. Retrieved 2014-04-22.
 "Sigma Plots". Nndc.bnl.gov. Retrieved 2014-04-22.
 "Sigma Periodic Table Browse". Nndc.bnl.gov. 2007-01-25. Retrieved 2014-04-22.
 "Enriched boric acid for pressurized water reactors" (PDF). EaglePicher Corporation. Archived from the original (PDF) on November 29, 2007. Retrieved September 25, 2008.
External links
Nuclear power
at Wikipedia's sister projects
Definitions from Wiktionary
Media from Wikimedia Commons
News from Wikinews
Quotations from Wikiquote
Texts from Wikisource
Textbooks from Wikibooks
Resources from Wikiversity
Further reading
Powers, D.A. (August 1, 1985). "Behavior of control rods during core degradation: pressurization of silver-indium-cadmium control rods". Office of Scientific and Technical Information, United States Department of Energy. Retrieved May 29, 2017.
Petti, D.A. (March 1, 1987). "Silver-indium-cadmium control rod behavior and aerosol formation in severe reactor accidents". Office of Scientific and Technical Information, United States Department of Energy. Retrieved May 29, 2017.
Steinbrueck, M.; Stegmaier, U. (May 6, 2010). "Experiments on silver-indium-cadmium control rod failure during severe accident sequences". Karlsruhe Institute of Technology. Retrieved May 29, 2017.
Authority control Edit this at Wikidata	
NDL: 01109833
Categories: AlloysNuclear power plant componentsNuclear safety and securityPressurized water reactors
Navigation menu
Not logged inTalkContributionsCreate accountLog inArticleTalkReadEditView historySearch
Search Wikipedia
Main page
Contents
Featured content
Current events
Random article
Donate to Wikipedia
Wikipedia store
Interaction
Help
About Wikipedia
Community portal
Recent changes
Contact page
Tools
What links here
Related changes
Upload file
Special pages
Permanent link
Page information
Wikidata item
Cite this page
Print/export
Download as PDF
Printable version

Languages
العربية
Deutsch
Español
Français
한국어
हिन्दी
Italiano
Русский
中文
13 more
Edit links
This page was last edited on 10 January 2020, at 21:34 (UTC).
Text is available under the Creative Commons Attribution-ShareAlike License; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. Wikipedia® is a registered trademark of the Wikimedia Foundation, Inc., a non-profit organization.
Privacy policyAbout WikipediaDisclaimersContact WikipediaDevelopersStatisticsCookie statementMobile viewWikimedia FoundationPowered by MediaWiki
"""

p=get_relevance_factor(s)
print(p)


# for i in range(0, n):
#     fheappush(heap1, (r-1,"abc"))
#     r-=1

# test fib heap running time
# heap1.decrease_key(a,0.001)
# heap1.decrease_key(b,0.002)
# print(a.key)
# c=heap1.extract_min()
# print(heap1.extract_min().key)
# kl=n

# start_time = time.time()
# while kl > 0:
#     m = heap1.extract_min()
#     print(m.key)
#     kl-=1
# print ("seconds run time for fib-heap-library", (time.time() - start_time))
# a=heap1.min
# heap1.decrease_key(a,-1)
# a=heap1.min
# print(a)
