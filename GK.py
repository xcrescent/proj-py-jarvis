import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeInput():
    inputString = input('Enter a command:')
    inputStrng = inputString.lower()
    print(f"You entered: {inputString}\n")  
    # inputStrng = takeInput().lower()

    if 'hello' in inputStrng:
        speak('Question 1. World Cup Cricket 2023 Venue . Answer: INDIA   . Question'+
            ''+''+'2. Headquarters of ISRO . Answer: Bengaluru   . Question'+
            ''+''+'3. Validity time of cheque. Answer: 3 Months  . Question'+
            ''+''+
            ''+''+'4. National Science Day. Answer: Feb 28  . Question'+
            ''+''+
            ''+''+'5. First Bank in India . Answer: Bank of Hindustan  . Question'+
            ''+''+
            ''+''+'6. Percentage of Nitrogen in air. Answer: 78%  . Question'+
            ''+''+
            ''+''+'7. First Olympic Games was held in . Answer: Athens,Gr  . Question'+
            ''+''+
            ''+''+'8. Which is the opponent team for the first test match of Sachin in 1989. Answer: Pakistan  . Question'+
            ''+''+
            ''+''+'9. What is shortcut key to expand browsing screen in web browser. Answer: F11  . Question'+
            ''+''+
            ''+''+'10. Shimla Agreement took place in. Answer: 1972  . Question'+
            ''+''+
            ''+''+'11. ASCII Stands For. Answer: American Standard Code for Information Interchange  . Question'+
            ''+''+
            ''+''+'12. What gases can be found on Saturn. Answer: Hydrogen and Helium  . Question'+
            ''+''+
            ''+''+'13. What is the process called in which Zinc Oxide is applied to metals to stop them from rusting. Answer: Galvanization  . Question'+
            ''+''+
            ''+''+'14. DBMS full form. Answer: Database Management System  . Question'+
            ''+''+
            ''+''+'15. Which fundamental right is guaranteed even to non-citizens of India. Answer: Article 21 . Answer: Right to Life & Personal Liberty  . Question'+
            ''+''+
            ''+''+'16. The Second Round Table Conference was conducted in which month of 1931. Answer: September  . Question'+
            ''+''+
            ''+''+'17. Who was awarded the 2015 Nobel Prize of Literature. Answer: Svetlana Alexievich  . Question'+
            ''+''+
            ''+''+'18. How many Fundamental Duties we have in our constitution. Answer: 11  . Question'+
            ''+''+
            ''+''+'19. Leucoderma (Safed Daag) treatment. Answer:  . Question'+
            ''+''+
            ''+''+'20. Confucius award 2016 was given to. Answer: Robert Mugabe of Zimbabwe  . Question'+
            ''+''+
            ''+''+'21. What is the full form of U N F C C C. Answer: United Nations Framework Convention on Climate Change  . Question'+
            ''+''+
            ''+''+'22. Recently, the Delhi Police launched an app for women in distress.The name of the app is. Answer: Himmat  . Question'+
            ''+''+
            ''+''+'23. Father of All India Services. Answer: Sardar Vallabhbhai Patel  . Question'+
            ''+''+
            ''+''+'24. Name of the operation that led to the capture and death of Osama Bin Laden. Answer: Operation Neptune Spear  . Question'+
            ''+''+
            ''+''+'25. Who started the Home Rule Movement in India. Answer: Annie Besant  . Question'+
            ''+''+
            ''+''+'26. Chenab, Jhelum are tributaries of which river. Answer: Indus  . Question'+
            ''+''+
            ''+''+"27. Winner of Women's Doubles Title at BNP Paribas Open Tournament in 2016. Answer: Sania Mirza & Martina Hingis . Question"+
            ''+''+
            ''+''+'28. Who is the only male in the National Women-s Commission. Answer: Alok Rawat  . Question'+
            ''+''+
            ''+''+'29. Who came up with the concept of properties of elements repeating as a property of their atomic number, as is arranged in the periodic table. Answer: Dmitri Mendeleev  . Question'+
            ''+''+
            ''+''+'30. Which organ removes nitrogenous compounds from the blood. Answer: Kidney  . Question'+
            ''+''+
            ''+''+'31. Rocket launch pad . Answer: Sriharikota  . Question'+
            ''+''+
            ''+''+'32. INS Vikrant was decommissioned in which year. Answer: 1997  . Question'+
            ''+''+
            ''+''+'33. What is study of soil called as. Answer: Pedology  . Question'+
            ''+''+
            ''+''+'34. In which year Aryabhatta was launched. Answer: 1975  . Question'+
            ''+''+
            ''+''+'35. While raining a type of smell comes known as. Answer: Ozone  . Question'+
            ''+''+
            ''+''+'36. Who is chairman of human rights commission. Answer: HL Dattu  . Question'+
            ''+''+
            ''+''+'37. What are number of balls in snooker. Answer: 22  . Question'+
            ''+''+
            ''+''+'38. Fastest century in test cricket match. Answer: Brendon Mccullum  . Question'+
            ''+''+
            ''+''+'39. Who is president of south Asian wrestling federation. Answer: Brij Bhushan Sharan Singh  . Question'+
            ''+''+
            ''+''+'40. Delhi is made capital in which year. Answer: 1911  . Question'+
            ''+''+
            ''+''+'41. World Vanya Prandi day. Answer: 6th october  . Question'+
            ''+''+
            ''+''+'42. Pakistani cricket umpire which has been banned for 5 years. Answer: Asad Rauf  . Question'+
            ''+''+
            ''+''+'43. The first animal domesticated by Neolithic people. Answer: Dog  . Question'+
            ''+''+
            ''+''+'44. What is the full form of NSA. Answer: National Security Agency  . Question'+
            ''+''+
            ''+''+'45. Who was first female Judge of High Court. Answer: Anna Chandy  . Question'+
            ''+''+
            ''+''+'46. Which gas is filled in balloons. Answer: Helium  . Question'+
            ''+''+
            ''+''+'47. Which Constitution Amendment was enacted by Indira Gandhi during the Emergency. Answer: 42nd Amendment  . Question'+
            ''+''+
            ''+''+'48. Who holds the record for the Fastest Test Hundred. Answer: Brendon McCullum  . Question'+
            ''+''+
            ''+''+'49. The President signed a proclamation under which article for imposing President-s Rule in Arunachal Pradesh. Answer: 356(1)  . Question'+
            ''+''+
            ''+''+'50. Jeevan Raksha Padak has how many categories. Answer: 3 (Sarvottam Jeevan Raksha Padak, Uttam Jeevan Raksha Padak, and Jeevan Raksha Padak)  . Question'+
            ''+''+
            ''+''+'51. Poona pact was signed in which year. Answer: 1932  . Question'+
            ''+''+
            ''+''+'52. Securities & Exchange Board of India (SEBI) was established in. Answer: 1988  . Question'+
            ''+''+
            ''+''+"53. India's victory over New Zealand in test match series in Mar-Apr, 2009 came after how many years. Answer: 41  Question"+
            ''+''+
            ''+''+'54. Who has been elected as the PM of Georgia on 29th December 2015. Answer: Giorgi Kvirikashvili  . Question'+
            ''+''+
            ''+''+'55. What is the age of the universe. Answer: 8 billion years  . Question'+
            ''+''+
            ''+''+"56. CBSE's latest mobile application for providing e-learning material is called. Answer: e-CBSE  Question"+
            ''+''+
            ''+''+'57. Who was the first female Muslim PM in the World. Answer: Benazir Bhutto  . Question'+
            ''+''+
            ''+''+'58. Gyan Peeth Award for 2015 is given for which book. Answer: Amruta  . Question'+
            ''+''+
            ''+''+'59. Dinosaur were present on earth in which age. Answer: Mesozoic Era  . Question'+
            ''+''+
            ''+''+'60. Who is the chairman of Yes Bank. Answer: Radha Singh  . Question'+
            ''+''+
            ''+''+'61. Atomic number of Oxygen . Answer: 8  . Question'+
            ''+''+
            ''+''+'62. Subhash chandra bose founded which party . Answer: All India Forward Bloc  . Question'+
            ''+''+
            ''+''+'63. The last king of chola dynasty . Answer: Rajendra Chola III  . Question'+
            ''+''+
            ''+''+'64. Who became the only Indian Governor-General . Answer: Rajagopalachari  . Question'+
            ''+''+
            ''+''+'65. Who has been honoured twice, with the 1903 Nobel Prize in Physics and the 1911 Nobel Prize in Chemistry. Answer: Marie Curie  . Question'+
            ''+''+
            ''+''+'66. The second airport in the National Capital Region of Delhi . Answer: Bhiwadi  . Question'+
            ''+''+
            ''+''+'67. First modern summer olympics . Answer: 1896  . Question'+
            ''+''+
            ''+''+'68. Statue unveiled by P.M Modi in UK . Answer: Basaveshwara  . Question'+
            ''+''+
            ''+''+'69. Alassane Ouattara is . Answer: President of Ivory Coas  . Question'+
            ''+''+
            ''+''+'70. Which of the following has atomic number 3. Answer: Lithium.  . Question'+
            ''+''+
            ''+''+'71. Kesari, Marathi newspaper founded by . Answer: Lokmanya Bal Gangadhar Tilak  . Question'+
            ''+''+
            ''+''+'72. World-s first cashless country. Answer: Sweden.  . Question'+
            ''+''+
            ''+''+'73. Gautam Buddha gave his first sermon. Answer: Sarnath.  . Question'+
            ''+''+
            ''+''+'74. First animal to go into space orbit. Answer: Dog . Answer: Laika  . Question'+
            ''+''+
            ''+''+'75. Science that deals with diseases particularly of men. Answer: Andrology.  . Question'+
            ''+''+
            ''+''+'76. Real founder of Gupta dynasty. Answer: Chandragupta 1.  . Question'+
            ''+''+
            ''+''+'77. Who among the following was a co-founder of Swaraj party. Answer: Motilal Nehru.  . Question'+
            ''+''+
            ''+''+'78. Indian Hockey team won in the Olympic in which year . Answer: 1928  . Question'+
            ''+''+
            ''+''+'79. President of South Asian Wrestling Federation . Answer: Brij Bhushan Singh  . Question'+
            ''+''+
            ''+''+'80. Aryabhata was launched in. Answer: 1975  . Question'+
            ''+''+
            ''+''+'81. Delhi became the capital of India in. Answer: 1931.  . Question'+
            ''+''+
            ''+''+'82. Who is the opposition leader in Rajya Sabha. Answer: Ghulam Nabi Azad  . Question'+
            ''+''+
            ''+''+'83. Anshu gupta Ramon Magsaysay Award winner . Answer: Founder of Goonj (NGO)  . Question'+
            ''+''+
            ''+''+'84. World Animal Day . Answer: October 4  . Question'+
            ''+''+
            ''+''+'85. Thomas cup related to . Answer: Badminton  . Question'+
            ''+''+
            ''+''+'86. 10 rupee and 125 rupee coin has been created for whom recently. Answer: Dr. R. Ambedkar  . Question'+
            ''+''+
            ''+''+'87. Mixed double Wimbledon champion 2015 . Answer: Martina Hingis and Leander Paes  . Question'+
            ''+''+
            ''+''+'88. Distance of light travelled in one year. Answer: 10 trillion Km  . Question'+
            ''+''+
            ''+''+'89. ASLV launched in. Answer: 1994  . Question'+
            ''+''+
            ''+''+'90. Radish is . Answer: an edible root  . Question'+
            ''+''+
            ''+''+'91. Red Planet . Answer: Mars  . Question'+
            ''+''+
            ''+''+'92. Study of the liver . Answer: Hepatology  . Question'+
            ''+''+
            ''+''+'93. Galvanization of Steel and iron is done by. Answer: Zinc.  . Question'+
            ''+''+
            ''+''+'94. Which of the following mountain comes under Biodiversity hotspot . Answer: Western Gha  . Question'+
            ''+''+
            ''+''+'95. Saraswati Samman award winner in 2014. Answer: Veerappa Moily  . Question'+
            ''+''+
            ''+''+'96. Belur Math located in. Answer: West Bengal  . Question'+
            ''+''+
            ''+''+'97. Who is the captain of T20 women-s world cup winner team in 2016. Answer: Stafanie Taylor (West Indies)  . Question'+
            ''+''+
            ''+''+'98. First civilian president of Myanmar. Answer: Htin Kya  . Question'+
            ''+''+
            ''+''+'99. Old name of ICC. Answer: Imperial Cricket Conference  . Question'+
            ''+''+
            ''+''+'100. Official language of Goa. Answer: Konkani  . Question'+
            ''+''+
            ''+''+'101. Distance between the Sun and the Earth . Answer: 6 million km  . Question'+
            ''+''+
            ''+''+'102. IIM recently opened in which state. Answer: Andhra Pradesh  . Question'+
            ''+''+
            ''+''+'103. Salar Jung Museum located in. Answer: Hyderabad  . Question'+
            ''+''+
            ''+''+'104. Indira Gandhi National centre for arts is in. Answer: New Delhi  . Question'+
            ''+''+
            ''+''+'105. Mizoram-s capital . Answer: Aizawl  . Question'+
            ''+''+
            ''+''+'106. Indian T20 Women-s team captain 2016 . Answer: Mithali Raj  . Question'+
            ''+''+
            ''+''+'107. World-s happiest Country . Answer: Denmark  . Question'+
            ''+''+
            ''+''+'108. Name of Pakistan Parliament . Answer: Majlis-e-Shoora  . Question'+
            ''+''+
            ''+''+'109. which gas is mostly present in Venus atmosphere. Answer: carbon dioxide  . Question'+
            ''+''+
            ''+''+'110. What is the most intelligent mammal on earth. Answer: Dolphins  . Question'+
            ''+''+
            ''+''+'111. Two atoms, ions or molecules that have the same electronic structure and same number of valence electrons is called . Answer: Isoelectronic  . Question'+
            ''+''+
            ''+''+'112. CDM stands for. Answer: Cash Deposit Machine  . Question'+
            ''+''+
            ''+''+'113. What is the normal temperature of a human body. Answer: 6-F (37-C)  . Question'+
            ''+''+
            ''+''+'114. Capital of Manipur . Answer: Imphal  . Question'+
            ''+''+
            ''+''+'115. Which element is used in nuclear fission to observe neutrons. Answer: Cadmium  . Question'+
            ''+''+
            ''+''+'116. Digestive acid in human body . Answer: HCL  . Question'+
            ''+''+
            ''+''+'117. Pankaj Advani bags 13th World Snooker Championship by defeating. Answer: Yan Bingtao of China  . Question'+
            ''+''+
            ''+''+'118. H.S.Prannoy related to . Answer: Badminton  . Question'+
            ''+''+
            ''+''+'119. Jaistambh located in. Answer: Raipur, Chhattisgarh  . Question'+
            ''+''+
            ''+''+'120. The old name of Allahabad . Answer: Prayag  . Question'+
            ''+''+
            ''+''+'121. Official language of Nagaland . Answer: English  . Question'+
            ''+''+
            ''+''+'122. Milkha singh is. Answer: flying Sikh  . Question'+
            ''+''+
            ''+''+'123. Chief Justice of India . Answer: Jagdish Singh Khehar  . Question'+
            ''+''+
            ''+''+'124. White flag is symbol of what. Answer: surrender  . Question'+
            ''+''+
            ''+''+'125. In 2015 the FDI limit in defence increased from 18% to what %. Answer: 49%  . Question'+
            ''+''+
            ''+''+'126. Santosh trophy is related to. Answer: Football  . Question'+
            ''+''+
            ''+''+'127. Smallest planet . Answer: Mercury  . Question'+
            ''+''+
            ''+''+'128. Where is the Pashupatinath temple. Answer: Nepal  . Question'+
            ''+''+
            ''+''+'129. Capital city of Syria. Answer: Damascus  . Question'+
            ''+''+
            ''+''+'130. Forbidden city of china situated at. Answer: Beijing  . Question'+
            ''+''+
            ''+''+'131. Who is appointed as the brand ambassador of "Atulya Bharat". Answer: Amitabh Bachchan  . Question'+
            ''+''+
            ''+''+'132. Bouncing back of rubber ball from a wall is related to (1st law of newton,2nd law of newton,3rd law of newton,None of the above). Answer: Newton-s 3rd law  . Question'+
            ''+''+
            ''+''+'133. Device used to measure current. Answer: Galvanometer  . Question'+
            ''+''+
            ''+''+'134. Which of the following awards is not received by Sachin tendulkar. Answer: Dhyan Chand Award  . Question'+
            ''+''+
            ''+''+'135. Who is H S Prannoy. Answer: badminton player  . Question'+
            ''+''+
            ''+''+'136. Prime Ministers who got Bharat Ratna award . Answer: Atal Bihari Vajpayee  . Question'+
            ''+''+
            ''+''+'137. BRICS Bank Name. Answer: NDB (New Development Bank)  . Question'+
            ''+''+
            ''+''+'138. Who is the founder of ABO Blood Group . Answer: Karl Landsteiner  . Question'+
            ''+''+
            ''+''+'139. What is the full of TCP in terms of Network . Answer: Transfer Control Protocol  . Question'+
            ''+''+
            ''+''+'140. What is the name of Largest moon of Pluto . Answer: Charon  . Question'+
            ''+''+
            ''+''+'141. Which is the largest moon in Solar system . Answer: Ganymede  . Question'+
            ''+''+
            ''+''+'142. When the AAP Party was established . Answer: 26 November 2012  . Question'+
            ''+''+
            ''+''+'143. Who is the founder of Twitter . Answer: Evan Williams, Noah Glass, Jack Dorsey, Biz Stone  . Question'+
            ''+''+
            ''+''+'144. Mary Kom belongs to which state. Answer: Manipur  . Question'+
            ''+''+
            ''+''+'145. In IPL Raina and Dhoni played to . Answer: Rajkot and pune  . Question'+
            ''+''+
            ''+''+'146. Indira point is located at. Answer: Andaman  . Question'+
            ''+''+
            ''+''+'147. Gagan Narang and Abhinav Bindra related to. Answer: Shooting  . Question'+
            ''+''+
            ''+''+'148. First satellite of India sent towards lunars is. Answer: Chandrayaan 1  . Question'+
            ''+''+
            ''+''+'149. The process of coating on the surface of a metal with zinc is called. Answer: Galvanisation  . Question'+
            ''+''+
            ''+''+'150. The scientist who got Nobel prize on malaria is. Answer: Sir Ronald Ross  . Question'+
            ''+''+
            ''+''+'151. Elisa is the test for AIDS but it is caused by virus. Answer: HIV  . Question'+
            ''+''+
            ''+''+'152. Narendra modi meets nawaz Sharif to surprise him at his Birthday at. Answer: Pakistan  . Question'+
            ''+''+
            ''+''+'153. Tooth enamel is made up of. Answer: calcium phospha  . Question'+
            ''+''+
            ''+''+'154. Birju maharaj composed a song for Deepika padukone in "Bajirao mastani" is a . Answer: kathak Dancer  . Question'+
            ''+''+
            ''+''+'155. Which national park has world-s two thirds one horned rhinos-Kaziranga National Park  . Question'+
            ''+''+
            ''+''+'156. Ginger is one of the following type. Answer: Underground stem  . Question'+
            ''+''+
            ''+''+'157. Eliminated Planet . Answer: Pluto  . Question'+
            ''+''+
            ''+''+'158. Qutub Minar, Alai Darwaza(magnificent gateway) built by. Answer: Ala-ud-din Khilji  . Question'+
            ''+''+
            ''+''+'159. Bulb filament is made up of. Answer: Tungsten  . Question'+
            ''+''+
            ''+''+'160. Google-s CEO . Answer: Sundar Pichai  . Question'+
            ''+''+
            ''+''+'161. Common salt chemical formula . Answer: NaCl  . Question'+
            ''+''+
            ''+''+'162. Which gas is used for flushing potato chips packet. Answer: Nitrogen.  . Question'+
            ''+''+
            ''+''+'163. Roger Federer belongs to . Answer: Switzerland.  . Question'+
            ''+''+
            ''+''+'164. Hubble Space telescope belongs to which country. Answer: USA.  . Question'+
            ''+''+
            ''+''+'165. Satish Dhawan Space center which state. Answer: Andhra Prade  . Question'+
            ''+''+
            ''+''+'166. Present Commerce and industry minister of India. Answer: Nirmala Sitharaman  . Question'+
            ''+''+
            ''+''+'167. Bhimbetka rock shelters are located at-Madhya Pradesh  . Question'+
            ''+''+
            ''+''+'168. Which actor will be with Rajinikanth in Enthiran 2. Answer: Arnold Schwarzenegger  . Question'+
            ''+''+
            ''+''+'169. Mouma Das is related to. Answer: Table Tennis  . Question'+
            ''+''+
            ''+''+'170. First human to travel into space. Answer: Yuri Gagarin  . Question'+
            ''+''+
            ''+''+'171. which metal is used for galvanising of iron . Answer: Zinc  . Question'+
            ''+''+
            ''+''+'172. Which country has the biggest constitution in the World. Answer: India  . Question'+
            ''+''+
            ''+''+'173. Shashank Subramanyam is related to. Answer: renowned exponent of the Bamboo Flute  . Question'+
            ''+''+
            ''+''+'174. Official language of Afghanistan. Answer: Pashto, Dari  . Question'+
            ''+''+
            ''+''+'175. Canada-s first space telescope . Answer: MOST  . Question'+
            ''+''+
            ''+''+'176. Gold is soluble in. Answer: Aqua Regia  . Question'+
            ''+''+
            ''+''+'177. Lalita Babar related to sports. Answer: Athletics  . Question'+
            ''+''+
            ''+''+'178. First Indian Woman Boxer to win Gold in Asian Games. Answer: Mary Kom  . Question'+
            ''+''+
            ''+''+'179. Blue Ray Disk Refer to which of the following. Answer: Storage disk  . Question'+
            ''+''+
            ''+''+'180. Which of the following is not a Board Game. Answer: Bridge  . Question'+
            ''+''+
            ''+''+'181. Which organisation held Cricket World Cup. Answer: International Cricket Council (ICC)  . Question'+
            ''+''+
            ''+''+'182. Who is first Indian to go Space. Answer: Rakesh Sharma  . Question'+
            ''+''+
            ''+''+'183. Where is International Renewable Energy Agency. Answer: Abu Dhabi  . Question'+
            ''+''+
            ''+''+'184. Best actor award in 88th Academy Awards. Answer: Leonardo Dicaprio  . Question'+
            ''+''+
            ''+''+'185. Rank of Mukesh Ambani in Forbes richest person 2016. Answer: 36  . Question'+
            ''+''+
            ''+''+'186. Arjuna Award 2015 in Kabaddi. Answer: Manjeet Chillar  . Question'+
            ''+''+
            ''+''+'187. Fullform of CT in CT scan . Answer: Computed Tomography  . Question'+
            ''+''+
            ''+''+'188. Who was the PM of India for two short periods following the deaths of Jawaharlal Nehru in 1964 and Lal Bahadur Shastri in 1966. Answer: Gulzarilal Nanda  . Question'+
            ''+''+
            ''+''+'189. CEC stands for . Answer: Chief Election Commission  . Question'+
            ''+''+
            ''+''+'190. Pakistan capital . Answer: Islamabad  . Question'+
            ''+''+
            ''+''+'191. Which is the Best picture in 88th Oscar Award. Answer: Spotlight  . Question'+
            ''+''+
            ''+''+'192. Who led the Bardoli Satyagraha. Answer: Sardar Vallabhai Patel  . Question'+
            ''+''+
            ''+''+'193. Full form of MRI. Answer: Magnetic Resource Imaging  . Question'+
            ''+''+
            ''+''+'194. Currency of Bangladesh. Answer: Taka  . Question'+
            ''+''+
            ''+''+'195. Mecca located in. Answer: Saudi Arabia  . Question'+
            ''+''+
            ''+''+'196. First woman cosmonaut in the world. Answer: Valentina Tereshkova  . Question'+
            ''+''+
            ''+''+'197. I work @ home is by which bank. Answer: ICICI Bank  . Question'+
            ''+''+
            ''+''+'198. Main raw material in glass . Answer: Silica  . Question'+
            ''+''+
            ''+''+'199. Sumitra Mahajan represents which constituency. Answer: Indore  . Question'+
            ''+''+
            ''+''+'200. Chera dynasty ruled which states of India. Answer: Kerala & Tamil Nadu  . Question'+
            ''+''+
            ''+''+'201. World Cancer Day . Answer: Feb 4  . Question'+
            ''+''+
            ''+''+'202. SBI previous name. Answer: Imperial Bank of India  . Question'+
            ''+''+
            ''+''+'203. Pluto discovered in the year. Answer: 2006  . Question'+
            ''+''+
            ''+''+'204. Jahangir was. Answer: 4th Mughal emperor  . Question'+
            ''+''+
            ''+''+'205. Head of the State Bank of India. Answer: Arundhati Bhattacharya  . Question'+
            ''+''+
            ''+''+'206. Black soil also called. Answer: Indian regurs  . Question'+
            ''+''+
            ''+''+'207. Bhopal gas tragedy results many people died, which gas exposed. Answer: methyl isocyanate  . Question'+
            ''+''+
            ''+''+'208. Rajatarangini related to which state. Answer: Kashmir  . Question'+
            ''+''+
            ''+''+'209. Which country won maximum number of FIFA World football cup-Brazil  . Question'+
            ''+''+
            ''+''+'210. What is blue moon. Answer: It is an additional full moon that appears in a subdivision of a year.  . Question'+
            ''+''+
            ''+''+'211. Unit of Force. Answer: Newton  . Question'+
            ''+''+
            ''+''+'212. A body which is completely or partially submerged in a fluid experiences an upward force called the. Answer: Buoyant Force  . Question'+
            ''+''+
            ''+''+'213. Name of E-mail inventor . Answer: Shiva Ayyadurai  . Question'+
            ''+''+
            ''+''+'214. Emergency imposed by. Answer: President  . Question'+
            ''+''+
            ''+''+'215. what is desalination. Answer: process of removing dissolved salts from water to produce freshwater from seawater  . Question'+
            ''+''+
            ''+''+'216. Wipro CEO . Answer: Abid Ali Z. Neemuchwala  . Question'+
            ''+''+
            ''+''+'217. Which is egypt-s largest pyramid. Answer: The Great Pyramid of Giza  . Question'+
            ''+''+
            ''+''+'218. Cristiano Ronaldo belongs to which country. Answer: Portugal  . Question'+
            ''+''+
            ''+''+'219. Supreme Court established in Which year. Answer: 1950  . Question'+
            ''+''+
            ''+''+'220. Gyroscope used in Which device. Answer: Smartphone  . Question'+
            ''+''+
            ''+''+'221. First Solar Powered Airport In India. Answer: Kochi  . Question'+
            ''+''+
            ''+''+'222. Who is the predecessor of Satya Nadella as CEO of Microsoft. Answer: Steve Ballmer  . Question'+
            ''+''+
            ''+''+'223. Which is known as Nerve Centre of Computer. Answer: Arithmetic Logic Unit  . Question'+
            ''+''+
            ''+''+'224. What is Dry Ice. Answer: Solid form of Carbon Dioxide  . Question'+
            ''+''+
            ''+''+'225. Who Invented Dynamite. Answer: Alfred Nobel  . Question'+
            ''+''+
            ''+''+'226. First Chinese Women went to Space. Answer: Liu Yang  . Question'+
            ''+''+
            ''+''+'227. Sound Measured in. Answer: Decibel  . Question'+
            ''+''+
            ''+''+'228. Which City is called Pink City . Answer: Jaipur  . Question'+
            ''+''+
            ''+''+'229. Netrani (also known as Pigeon Island) is a small island of India located in. Answer: The Arabian Sea  . Question'+
            ''+''+
            ''+''+'230. Who constructed the Chennakesava swamy temple . Answer: Hoysala Empire King Vishnuvardhana  . Question'+
            ''+''+
            ''+''+'231. Who is the author of book "Straight Drive". Answer:  Sunil Gavaskar  . Question'+
            ''+''+
            ''+''+'232. Which is India-s first defence satellite. Answer: GSAT-7  . Question'+
            ''+''+
            ''+''+'233. Who is pass the railway budget in 1947. Answer: John Mathai  . Question'+
            ''+''+
            ''+''+'234. Who is inventor of Video Games. Answer: Ralph Henry Baer  . Question'+
            ''+''+
            ''+''+'235. Quantity of blood in human being. Answer:  . Question'+
            ''+''+
            ''+''+'236. Museum of nobel prize in. Answer: Sweden  . Question'+
            ''+''+
            ''+''+'237. Who won Man Booker Prize 2015. Answer: Marlon James  . Question'+
            ''+''+
            ''+''+'238. What is the full form of ATM. Answer: Automated Teller Machine  . Question'+
            ''+''+
            ''+''+'239. Formula of chalk. Answer: CaCO3 (Calcium Carbonate)  . Question'+
            ''+''+
            ''+''+'240. Queen of Arabian Sea. Answer: Kochi  . Question'+
            ''+''+
            ''+''+'241. Date of partition of India. Answer: 15 Aug 1947  . Question'+
            ''+''+
            ''+''+'242. First Capital of Sri Lanka. Answer: Anuradhapura  . Question'+
            ''+''+
            ''+''+'243. Padma Bhushan in sports given to. Answer: Saina Nehwal  . Question'+
            ''+''+
            ''+''+'244. Combination of star. Answer: which type of gas. Answer:  . Question'+
            ''+''+
            ''+''+'245. Stainless Steel invented by. Answer: Harry Brearley  . Question'+
            ''+''+
            ''+''+'246. Commonwealth games 2022. Answer: Durban, SA  . Question'+
            ''+''+
            ''+''+'247. Who called guru dev 1st time to Rabindranath Tagore. Answer: Mahatma Gandhi  . Question'+
            ''+''+
            ''+''+'248. Ozone formula. Answer: O3  . Question'+
            ''+''+
            ''+''+'249. AAP was established at. Answer: Nov 26,2012  . Question'+
            ''+''+
            ''+''+'250. 7. Prime Ministers of India have awarded the Bharat Ratna . Answer: Jawaharlal Nehru, Indira Gandhi, Rajiv Gandhi, Morarji Desai, Lal Bahadur Shastri, Gulzarilal Nanda and Atal Bihari Vajpayee  . Question'+
            ''+''+
            ''+''+'251. Japan Parliament name . Answer: Diet  . Question'+
            ''+''+
            ''+''+'252. Who is recognized as the greatest of the Early Cholas. Answer: Karikalan  . Question'+
            ''+''+
            ''+''+'253. Old name of Singapore . Answer: Singa Pura  . Question'+
            ''+''+
            ''+''+'254. Madurai is situated on which river. Answer: Vaigai  . Question'+
            ''+''+
            ''+''+'255. Radioactivity discovered by. Answer: Henri Becquerel  . Question'+
            ''+''+
            ''+''+'256. Which state has the largest forest cover in India. Answer: Madhya Pradesh  . Question'+
            ''+''+
            ''+''+'257. Largest Mangrove forest in India . Answer: Sundarbans  . Question'+
            ''+''+
            ''+''+'258. AIMS hospital come up in Maharashtra. Answer: Nagpur  . Question'+
            ''+''+
            ''+''+'259. India-s First Supercomputer . Answer: PARAM 8000  . Question'+
            ''+''+
            ''+''+'260. The human body contains salt . Answer: 0.4% of the body-s weigh  . Question'+
            ''+''+
            ''+''+'261. Which temple is fully constructed in granite. Answer: Brihadeshwara temple  . Question'+
            ''+''+
            ''+''+'262. 23rd Governor of RBI . Answer: Raghuram Rajan  . Question'+
            ''+''+
            ''+''+'263. ICC number 1 test player. Answer: Steve Smith  . Question'+
            ''+''+
            ''+''+'264. Who is the largest serving Chief Minister in India . Answer: Pawan Chamling  . Question'+
            ''+''+
            ''+''+'265. Notre Dam Cathedral is located at . Answer: Paris  . Question'+
            ''+''+
            ''+''+'266. The inventor of fountain pen . Answer: Petrache Poenaru  . Question'+
            ''+''+
            ''+''+'267. MMU. Answer: Memory Management Unit  . Question'+
            ''+''+
            ''+''+'268. Who is inventor of revolver . Answer: Samuel Colt  . Question'+
            ''+''+
            ''+''+'269. River flows from Tibet. Answer: Sutlej  . Question'+
            ''+''+
            ''+''+'270. Atomic number is equal to. Answer: no of protons  . Question'+
            ''+''+
            ''+''+'271. Frontier Gandhi. Answer: Abdul Gaffar Khan  . Question'+
            ''+''+
            ''+''+'272. What is SI unit of force . Answer: Newton  . Question'+
            ''+''+
            ''+''+'273. MRP. Answer: Maximum Retail Price  . Question'+
            ''+''+
            ''+''+'274. Fethiye island is located at . Answer: Turkey  . Question'+
            ''+''+
            ''+''+'275. The study of heat is known as . Answer: Thermodynamics  . Question'+
            ''+''+
            ''+''+'276. Richest person as per Forbes global list. Answer: Carlos Slim  . Question'+
            ''+''+
            ''+''+'277. Who invented Fountain Pen. Answer: Petrache Poenaru  . Question'+
            ''+''+
            ''+''+'278. Who was the first ruler of Vijayanagara empire . Answer: Hari Hara Bukka  . Question'+
            ''+''+
            ''+''+'279. Replanting in forest is called . Answer: Reforestation  . Question'+
            ''+''+
            ''+''+'280. What is the study of environment . Answer: Ecology  . Question'+
            ''+''+
            ''+''+'281. King of Pallava Dynasty who wrote stories. Answer: Narasimhavarman I  . Question'+
            ''+''+
            ''+''+'282. Highest statue of Christ is located at. Answer: Rio de Janeiro  . Question'+
            ''+''+
            ''+''+'283. PA Sangma served as a Lok Sabha speaker in which year. Answer: 1996 to 1998  . Question'+
            ''+''+
            ''+''+'284. What does MRP means . Answer: Maximum Retail Price  . Question'+
            ''+''+
            ''+''+'285. ICC president. Answer: Zaheer Abbas  . Question'+
            ''+''+
            ''+''+'286. What is highest possible score in ten-pin bowling . Answer: 300  . Question'+
            ''+''+
            ''+''+'287. Mouse is invented by. Answer: Douglas Engelbart  . Question'+
            ''+''+
            ''+''+'288. Supreme Commander of Indian Defence Services. Answer: President  . Question'+
            ''+''+
            ''+''+'289. Longest bridge of world is in which country. Answer: China  . Question'+
            ''+''+
            ''+''+'290. Right to freedom and liberty in which article of constitution. Answer: Article 21  . Question'+
            ''+''+
            ''+''+'291. Current chief of election commission. Answer: Nasim Zaidi  . Question'+
            ''+''+
            ''+''+'292. Largest princely state during Indian Independence. Answer: Hyderabad  . Question'+
            ''+''+
            ''+''+'293. Railway budget 2016 presented by. Answer: Suresh Prabhu  . Question'+
            ''+''+
            ''+''+'294. Which bacteria converts milk to curd. Answer: Lactobacillus bacteria  . Question'+
            ''+''+
            ''+''+'295. UHT full form. Answer: Ultra High Temperature  . Question'+
            ''+''+
            ''+''+'296. Who Chinese came to India during Guptas period. Answer: Fa Hien  . Question'+
            ''+''+
            ''+''+'297. Saina Nehwal. Answer: Badminton  . Question'+
            ''+''+
            ''+''+'298. Rani laxmi bai died at which place. Answer: Gwalior  . Question'+
            ''+''+
            ''+''+'299. Brain of computer. Answer: C.U.  . Question'+
            ''+''+
            ''+''+'300. Muhammad Bin Tughlaq transferred from Delhi to. Answer: Daultabad  . Question'+
            ''+''+
            ''+''+'301. Largest silk producer state of India. Answer: Karnataka  . Question'+
            ''+''+
            ''+''+'302. Goecha La pass is in which state. Answer: Sikkim  . Question'+
            ''+''+
            ''+''+'303. Nitrogen fixing bacteria. Answer: Microorganisms  . Question'+
            ''+''+
            ''+''+'304. Who was appointed as M.D and CEO of central Mine planning & Design institute Ltd (CMPDI). Answer: Shekhar Sharan  . Question'+
            ''+''+
            ''+''+'305. Who has won the sangita kalanidhi award for 2015 . Answer: Sanjay Subrahmanyan  . Question'+
            ''+''+
            ''+''+'306. SPM. Answer: Scanning Probe Microscope  . Question'+
            ''+''+
            ''+''+'307. Which is Digital State of India. Answer: Kerala  . Question'+
            ''+''+
            ''+''+'308. Who is CEO of Flipkart. Answer: Binny Bansal  . Question'+
            ''+''+
            ''+''+'309. No.of bones in human adult. Answer: 206  . Question'+
            ''+''+
            ''+''+'310. Gas in which we live in breathe. Answer: Carbon dioxide  . Question'+
            ''+''+
            ''+''+'311. Laughing gas. Answer: Nitrous oxide  . Question'+
            ''+''+
            ''+''+'312. Highest bridge on which river. Answer: Bhagirathi  . Question'+
            ''+''+
            ''+''+'313. Maximum silk in India produced by. Answer: Karnataka  . Question'+
            ''+''+
            ''+''+'314. First chocolate made by. Answer: Hernan Cortes  . Question'+
            ''+''+
            ''+''+'315. Current president of pakistan. Answer: Mamnoon Hussain  . Question'+
            ''+''+
            ''+''+'316. Most poisonous fish in world. Answer: pufferfish  . Question'+
            ''+''+
            ''+''+'317. PM who hoisted tricolor maximum times. Answer: Jawaharlal Nehru  . Question'+
            ''+''+
            ''+''+'318. To kill a mocking word book written by. Answer: Lee Harper  . Question'+
            ''+''+
            ''+''+'319. Delhi-s only woman ruler. Answer: Razia Sultan  . Question'+
            ''+''+
            ''+''+'320. Golden rock temple (kyaiktiyo pagoda). Answer: Myanmar  . Question'+
            ''+''+
            ''+''+'321. 2016 Australian open women-s double. Answer: sania mirza and martina hingis  . Question'+
            ''+''+
            ''+''+'322. 8 world heritage day. Answer: 18 april  . Question'+
            ''+''+
            ''+''+'323. Dipika karmakar. Answer: gymnastic  . Question'+
            ''+''+
            ''+''+'324. Great grand old lady of bollywood. Answer: Johra Sehgal  . Question'+
            ''+''+
            ''+''+'325. Atmospheric pressure measured by which instrument. Answer: barometer  . Question'+
            ''+''+
            ''+''+'326. World-s most energy efficient city. Answer: reykjavik, Iceland  . Question'+
            ''+''+
            ''+''+'327. Function of hydro power plant. Answer: It converts kinetic energy into electrical energy  . Question'+
            ''+''+
            ''+''+'328. APGAR Score is test to summarize. Answer: To Summarise Health of Newborn Babies  . Question'+
            ''+''+
            ''+''+'329. One question related to bio (who developed genes ). Answer:  . Question'+
            ''+''+
            ''+''+'330. Famous temple of buddha in asia (borobudur). Answer: Indonesia  . Question'+
            ''+''+
            ''+''+'331. 1987 Australian world cup winner team captain. Answer: Allan border  . Question'+
            ''+''+
            ''+''+'332. Black gold. Answer: coal  . Question'+
            ''+''+
            ''+''+'333. BARC director. Answer: sekhar basu  . Question'+
            ''+''+
            ''+''+'334. Prime content of diamond. Answer: carbon  . Question'+
            ''+''+
            ''+''+'335. Which on is a program. Answer: Tbasic  . Question'+
            ''+''+
            ''+''+'336. Hottest planet. Answer: venus  . Question'+
            ''+''+
            ''+''+'337. Who is the 8th CM of Arunachal Pradesh. Answer: Kalikho Pul  . Question'+
            ''+''+
            ''+''+'338. Abhishek verma belongs to sport. Answer: Archery  . Question'+
            ''+''+
            ''+''+'339. Who was founder of Pal Dynasty. Answer: Gopal  . Question'+
            ''+''+
            ''+''+'340. Pacemaker related to which organ. Answer: Heart  . Question'+
            ''+''+
            ''+''+'341. How many candidates are nominated by President in Rajya Sabha. Answer: 12  . Question'+
            ''+''+
            ''+''+'342. Osama Bin Laden killed at which place. Answer: Abbottabad, Pakistan  . Question'+
            ''+''+
            ''+''+'343. Nathula Pass located at. Answer: Gangtok, Sikkim  . Question'+
            ''+''+
            ''+''+'344. Golconda Fort . Answer: Hyderabad  . Question'+
            ''+''+
            ''+''+'345. Assigned Amount Unit (AAU) is . Answer: "Kyoto unit" or "carbon credit" representing an allowance to emit greenhouse gases  . Question'+
            ''+''+
            ''+''+'346. Largest Tiger Reserve in India. Answer: Nagarjunsagar-Srisailam  . Question'+
            ''+''+
            ''+''+'347. Who was the viceroy when India got Independence. Answer: Lord Mountbatten  . Question'+
            ''+''+
            ''+''+'348. India-s first district with high-speed rural broadband network(NOFN). Answer: Idukki, kerala  . Question'+
            ''+''+
            ''+''+'349. Father of Indian Surgery . Answer: Sushruta  . Question'+
            ''+''+
            ''+''+'350. Name of International  Airport  in  India  which  runs  by  Solar  power. Answer:  Cochin International Airport  . Question'+
            ''+''+
            ''+''+'351. World Wide Web founder. Answer: Tim Berners Lee  . Question'+
            ''+''+
            ''+''+'352. When was PSLV Launched for the first time. Answer:  . Question'+
            ''+''+
            ''+''+'353. Election Commission does not conduct election to. Answer:  . Question'+
            ''+''+
            ''+''+'354. Jami Masjid . Answer: Delhi  . Question'+
            ''+''+
            ''+''+'355. World-s First Artificial Satellite . Answer: Sputnik I  . Question'+
            ''+''+
            ''+''+'356. Indian ambassador to UK. Answer: H.E.Mr.Navtej Sarna  . Question'+
            ''+''+
            ''+''+'357. The total amount that can be claimed under PRADHAN MANTRI SURAKSHA BIMA YOJANA policy is. Answer:  INR 2 lakh  . Question'+
            ''+''+
            ''+''+'358. Virupaksha Temple . Answer: Hampi  . Question'+
            ''+''+
            ''+''+'359. Sri Lanka got Independence in which year. Answer: 1948  . Question'+
            ''+''+
            ''+''+'360. Purpose of SAMANVAY. Answer: to help Member of Parliament-s (MPs) to utilise relevant schemes in the planning and implementation of Sansad Adarsh Gram Yojna(SAGY.)  . Question'+
            ''+''+
            ''+''+'361. Cultural Ambassador for seychelles . Answer: R.Rahman  . Question'+
            ''+''+
            ''+''+'362. Why control rods  are  used  in  nuclear  reactors. Answer:  to  control  the  fission  rate  of uranium and plutonium  . Question'+
            ''+''+
            ''+''+'363. One can-t see distant objects . Answer: Miopia  . Question'+
            ''+''+
            ''+''+'364. What is the present emission standard. Answer: Bharat Stage IV(BS-IV).  . Question'+
            ''+''+
            ''+''+'365. Who is the last viceroy before constitution came into effect. Answer:  . Question'+
            ''+''+
            ''+''+'366. Tidal Port . Answer: Kutch, Gujarat  . Question'+
            ''+''+
            ''+''+'367. The Tungabhadra is the main tributary of the. Answer: Krishna River  . Question'+
            ''+''+
            ''+''+'368. Fatehpur Sikri in . Answer: UP  . Question'+
            ''+''+
            ''+''+'369. Charminar Monument in . Answer: Hyderabad  . Question'+
            ''+''+
            ''+''+'370. IMF Chief. Answer: Christine Lagarde  . Question'+
            ''+''+
            ''+''+'371. CMOS Stands for. Answer: Complementary Metal-Oxide Semiconductor  . Question'+
            ''+''+
            ''+''+'372. Operation Smile is related to. Answer: missing Children  . Question'+
            ''+''+
            ''+''+'373. Humayun-s Tomb located in. Answer: New Delhi  . Question'+
            ''+''+
            ''+''+'374. Number of bones in spinal cord. Answer: 33  . Question'+
            ''+''+
            ''+''+'375. How many days did the battle of Mahabharata last. Answer: 18 days  . Question'+
            ''+''+
            ''+''+'376. Kalindi river is also known as . Answer: Yamuna  . Question'+
            ''+''+
            ''+''+'377. The name given to a series of satellites launched by ISRO. Answer: Rohini  . Question'+
            ''+''+
            ''+''+'378. First Female President of Nepal . Answer: Bidhya Devi Bhandari  . Question'+
            ''+''+
            ''+''+'379. What is the Rank of India in Corruption Index 2015. Answer: 76  . Question'+
            ''+''+
            ''+''+'380. Uniform civil code of India . Answer: Article-44  . Question'+
            ''+''+
            ''+''+'381. Prime Minister of Nepal . Answer: Khadga Prasad Sharma Oli  . Question'+
            ''+''+
            ''+''+'382. FIFA ballon d-or award 2015. Answer: Lionel Messi  . Question'+
            ''+''+
            ''+''+'383. Physical Research Laboratory was founded by. Answer: Vikram Sarabhai  . Question'+
            ''+''+
            ''+''+'384. State with Maximum boundaries with other states. Answer: UP  . Question'+
            ''+''+
            ''+''+'385. Who was the first President of the US. Answer: George Washington  . Question'+
            ''+''+
            ''+''+'386. X ray Inventor. Answer: Wilhelm Conrad Roentgen  . Question'+
            ''+''+
            ''+''+'387. Commonwealth Games 2014 . Answer: Glasgow, Switzerland  . Question'+
            ''+''+
            ''+''+'388. Which of the following is the lightest gas. Answer: Helium  . Question'+
            ''+''+
            ''+''+'389. Muhammad Hidayatullah . Answer: 11th Chief Justice of India  . Question'+
            ''+''+
            ''+''+'390. An ecotone is a. Answer: transition area between two biomes  . Question'+
            ''+''+
            ''+''+'391. First Woman Prime minister of Sri Lanka. Answer: Mrs Sirima Bandaranaike  . Question'+
            ''+''+
            ''+''+'392. Star shines due to. Answer: thermonuclear fusion  . Question'+
            ''+''+
            ''+''+'393. First muslim Woman President of the world . Answer: Benazir Bhutto  . Question'+
            ''+''+
            ''+''+'394. FIFA U-20 World Cup. Answer: New Zealand  . Question'+
            ''+''+
            ''+''+'395. First Chairman of the Banks Board Bureau. Answer: Vinod Rai  . Question'+
            ''+''+
            ''+''+'396. G20 Summit . Answer: Turkey  . Question'+
            ''+''+
            ''+''+'397. First Female Judge of High Court . Answer: Justice Anna Chandy  . Question'+
            ''+''+
            ''+''+'398. How many constellations are named. Answer: 88  . Question'+
            ''+''+
            ''+''+'399. The title Kaiser-e-Hind was given by the British Government to whom. Answer: Mahatma Gandhi  . Question'+
            ''+''+
            ''+''+'400. Modern Agra was founded by. Answer: Sikandar Lodhi  . Question'+
            ''+''+
            ''+''+'401. First Women President of Indian National Congress . Answer: Annie Besant  . Question'+
            ''+''+
            ''+''+'402. Ajanta Caves . Answer: Maharashtra  . Question'+
            ''+''+
            ''+''+'403. Formic acid found in . Answer: Ants  . Question'+
            ''+''+
            ''+''+'404. Telangana state has been formed during. Answer: 15th lok sabha  . Question'+
            ''+''+
            ''+''+'405. Forest Conservation Act. Answer: 1980  . Question'+
            ''+''+
            ''+''+'406. The transition of a substance directly from the solid to the gas phase without passing through the intermediate liquid phase . Answer: Sublimation  . Question'+
            ''+''+
            ''+''+'407. Grapes expand when you soak it in water. Answer: It is due to Osmosis  . Question'+
            ''+''+
            ''+''+'408. ISRO . Answer: Indian Space Research Organization  . Question'+
            ''+''+
            ''+''+'409. Maharashtra-s tiger ambassador . Answer: Amitabh Bachchan  . Question'+
            ''+''+
            ''+''+'410. BCCI Cricketer of the year 2015 . Answer: Virat Kohli  . Question'+
            ''+''+
            ''+''+'411. Study of humans . Answer: Anthropology  . Question'+
            ''+''+
            ''+''+'412. Maha bodhi temple is located at. Answer: Bodh Gaya  . Question'+
            ''+''+
            ''+''+'413. M.A chidambaram trophy best woman cricketer 2015. Answer: Mithali Raj  . Question'+
            ''+''+
            ''+''+'414. Red Fort built by. Answer: Shah Jahan  . Question'+
            ''+''+
            ''+''+'415. saurology is the study of. Answer: Lizards  . Question'+
            ''+''+
            ''+''+'416. What is the largest cell in our human body. Answer:  . Question'+
            ''+''+
            ''+''+'417. kudankulam nuclear power plant . Answer: Tamil Nadu  . Question'+
            ''+''+
            ''+''+'418. DVD stands for. Answer: Digital Video/Versatile Disc  . Question'+
            ''+''+
            ''+''+'419. Who will declare financial emergency. Answer: The President  . Question'+
            ''+''+
            ''+''+'420. Iron Man of India . Answer: Sardar Vallabhai Patel  . Question'+
            ''+''+
            ''+''+'421. Study of map is called. Answer: Cartography  . Question'+
            ''+''+
            ''+''+'422. Volley ball team has. Answer: Six players  . Question'+
            ''+''+
            ''+''+'423. Indira Gandhi tulip garden . Answer: J&K  . Question'+
            ''+''+
            ''+''+'424. Hindi Day . Answer: January 10  . Question'+
            ''+''+
            ''+''+'425. Unit of Pressure . Answer: Pascal  . Question'+
            ''+''+
            ''+''+'426. First Computer Programmer. Answer: Ada Lovelace  . Question'+
            ''+''+
            ''+''+'427. Study of Spider. Answer: Arachnology  . Question'+
            ''+''+
            ''+''+'428. 2016 olympics . Answer: Rio de Janeiro, Brazil  . Question'+
            ''+''+
            ''+''+'429. Capital of Arunachal Pradesh . Answer: Itanagar  . Question'+
            ''+''+
            ''+''+'430. Kanha National Park . Answer: MP  . Question'+
            ''+''+
            ''+''+'431. Indira Gandhi Botanical Garden located. Answer: Raebareli, UP  . Question'+
            ''+''+
            ''+''+'432. Who is the captain of women hockey team. Answer: Ritu Rani  . Question'+
            ''+''+
            ''+''+'433. Amalgam is a mixture of metal with which substance. Answer: Mercury  . Question'+
            ''+''+
            ''+''+'434. which of the following is not an inert gas..Ne,he,XE,H. Answer: Hydrogen  . Question'+
            ''+''+
            ''+''+'435. AIDS Day . Answer: December 1  . Question'+
            ''+''+
            ''+''+'436. US Open Women Doubles winner . Answer: Sania Mirza and Martina Hingis  . Question'+
            ''+''+
            ''+''+'437. First transistor invented in . Answer: 1947  . Question'+
            ''+''+
            ''+''+'438. Laughing Gas . Answer: Nitrous oxid  . Question'+
            ''+''+
            ''+''+'439. Normal blood pressure of human body. Answer: 80/120.  . Question'+
            ''+''+
            ''+''+'440. Mansarovar lake situated at. Answer: Tib  . Question'+
            ''+''+
            ''+''+'441. Rural Development Institute is situated at. Answer: Hyderabad.  . Question'+
            ''+''+
            ''+''+'442. The statement "Every citizen of our country is corrupted" given by. Answer: Lord Cornwallis  . Question'+
            ''+''+
            ''+''+'443. Popular dance of Tamilnadu. Answer: Bharatanatyam  . Question'+
            ''+''+
            ''+''+'444. World population day. Answer: July 11th.  . Question'+
            ''+''+
            ''+''+'445. Composer of Raghuvamsa. Answer: Kalidasa  . Question'+
            ''+''+
            ''+''+'446. Currency of Myanmar. Answer: Burmese kyat  . Question'+
            ''+''+
            ''+''+'447. Sardar Sarovar pariyojana belongs to which state. Answer: Gujara  . Question'+
            ''+''+
            ''+''+'448. World Health Day . Answer: April 7  . Question'+
            ''+''+
            ''+''+'449. Lingraj Temple situated at. Answer: Bhubaneswar.  . Question'+
            ''+''+
            ''+''+'450. Golf invented in which country . Answer: Scotland  . Question'+
            ''+''+
            ''+''+'451. Hridaynath mangeshkar award 2015 . Answer: R.Rahman  . Question'+
            ''+''+
            ''+''+'452. Which Party was founded by Subhash Chandra Bose in the Year 1939 after he broke away from the congress. Answer: All India Forward Bloc  . Question'+
            ''+''+
            ''+''+'453. Smallpox vaccine discovered by. Answer: Edward Jenner  . Question'+
            ''+''+
            ''+''+'454. LPG gas stored in. Answer: liquid form  . Question'+
            ''+''+
            ''+''+'455. National human right chairperson of India. Answer: HL Dattu  . Question'+
            ''+''+
            ''+''+'456. Asia cup cricket 2015 winner. Answer: India  . Question'+
            ''+''+
            ''+''+'457. who was elected as second time chief of UN in 2011. Answer: Ban ki moon  . Question'+
            ''+''+
            ''+''+'458. Who is the chairman of Bank Board Bureau. Answer: Vinod Rai  . Question'+
            ''+''+
            ''+''+'459. PCB stands for. Answer: Printed circuit board  . Question'+
            ''+''+
            ''+''+'460. Who was Prime Minister of Bangladesh in 1971. Answer: Tajuddin Ahmad  . Question'+
            ''+''+
            ''+''+'461. Brand ambassador of TATA motors. Answer: Lionel Messi  . Question'+
            ''+''+
            ''+''+'462. When East India company came to India. Answer: 1600  . Question'+
            ''+''+
            ''+''+'463. Azad hind Fauz formation year. Answer: 1943  . Question'+
            ''+''+
            ''+''+'464. Netware belongs to which country. Answer: India  . Question'+
            ''+''+
            ''+''+'465. Author of the Novel "A Brief History of Seven Killings". Answer: Marlon James  . Question'+
            ''+''+
            ''+''+'466. Which one is fastest memory. Answer: Cache  . Question'+
            ''+''+
            ''+''+'467. Yogeshwar Dutt is from which field. Answer: Wrestler  . Question'+
            ''+''+
            ''+''+'468. In UNESCO world heritage which is not included Mountain railways of India. Answer: kashmir railway  . Question'+
            ''+''+
            ''+''+'469. First man to go to space. Answer: Yuri Gagarin  . Question'+
            ''+''+
            ''+''+'470. Which one is fastest memory. Answer: Cache  . Question'+
            ''+''+
            ''+''+'471. Yogeshwar Dutt is from which field. Answer: Wrestler  . Question'+
            ''+''+
            ''+''+'472. Effect of pressure on sound. Answer: no change  . Question'+
            ''+''+
            ''+''+"473. To the 'Brink and the Bank book':india's 1991 story was written by. Answer: Jairam Ramesh  . Question"+
            ''+''+
            ''+''+'474. Second Battle of Panipat . Answer: 1556  . Question'+
            ''+''+
            ''+''+'475. Which country celebrate Independence day on 19th August . Answer: Afghanistan  . Question'+
            ''+''+
            ''+''+'476. Dimension of volleyball court . Answer: 18 metre (59 Feet)  . Question'+
            ''+''+
            ''+''+'477. 8th UN secretary general . Answer: Ban-Ki-moon  . Question'+
            ''+''+
            ''+''+'478. After entering Bangladesh, the main branch of the Ganges is known as the. Answer: River Padma . Question'+
            ''+''+
            ''+''+'479. First Anglo-Sikh War was fought between the Sikh Empire and the East India Company between. Answer:  1845 and 1846  . Question'+
            ''+''+
            ''+''+'480. Losoong festival is celebrated in which state. Answer: Sikkim  . Question'+
            ''+''+
            ''+''+'481. Leprosy is also called. Answer: Hansen-s Disease  . Question'+
            ''+''+
            ''+''+'482. Who is the father of Modern Genetics. Answer: Gregor Mendel  . Question'+
            ''+''+
            ''+''+'483. Louis Pasteur invented vaccine. Answer: Rabies  . Question'+
            ''+''+
            ''+''+'484. National Air Quality Index is based on how many pollutants. Answer: Eight  . Question'+
            ''+''+
            ''+''+'485. Main motive for Civil Disobedience Movement in 1929. Answer: Against unjust laws  . Question'+
            ''+''+
            ''+''+'486. LIGO related to . Answer: Laser  . Question'+
            ''+''+
            ''+''+'487. British decide to grant independence to India. Answer: 1947  . Question'+
            ''+''+
            ''+''+'488. Who is the Founder of Swaraj Party. Answer: Chittaranjan Das  . Question'+
            ''+''+
            ''+''+'489. Laughing gas is. Answer: Nitrous Oxide  . Question'+
            ''+''+
            ''+''+'490. Dwarf planet is. Answer: Pluto  . Question'+
            ''+''+
            ''+''+'491. Shortcut of Paste in MS Word. Answer: Ctrl+V  . Question'+
            ''+''+
            ''+''+'492. Currency of Myanmar. Answer: Kyat  . Question'+
            ''+''+
            ''+''+'493. Who built Jantar Mantar of Delhi. Answer: Maharaja Jai Singh  . Question'+
            ''+''+
            ''+''+'494. Popular dance of TamilNadu. Answer: Bharatnatyam  . Question'+
            ''+''+
            ''+''+'495. Leprosy also known as. Answer: Hansen-s disease  . Question'+
            ''+''+
            ''+''+'496. Ligo, a mission is related to. Answer: Black Holes  . Question'+
            ''+''+
            ''+''+'497. How generator works. Answer: Mechanical to electrical Energy  . Question'+
            ''+''+
            ''+''+'498. Smiling Buddha Mission. Answer: India-s first successful nuclear bomb test  . Question'+
            ''+''+
            ''+''+'499. What is Calcium Hydroxide. Answer: Lime Water  . Question'+
            ''+''+
            ''+''+'500. Another Name of Badshah Khan. Answer: Abdul Ghaffar Khan  . Question'+
            ''+''+
            ''+''+'501. First woman DG of paramilitary forces. Answer: Archana Ramasundram  . Question'+
            ''+''+
            ''+''+'502. Syed Modi Grand prix held on which place. Answer: Lucknow  . Question'+
            ''+''+
            ''+''+'503. When was Microsoft founded. Answer: 1975  . Question'+
            ''+''+
            ''+''+'504. Start Up India launch year. Answer: 2016  . Question'+
            ''+''+
            ''+''+'505. Which is not a gland(options: Liver,gall bladder,Pituitary,Adrenal). Answer: Gall Bladder  . Question'+
            ''+''+
            ''+''+'506. Parliament Construction year. Answer: 1927  . Question'+
            ''+''+
            ''+''+'507. Nephron Belongs to. Answer: Kidney  . Question'+
            ''+''+
            ''+''+'508. British Rule was ended on which year. Answer: 1947  . Question'+
            ''+''+
            ''+''+'509. Mars is also known as. Answer: Red Planet  . Question'+
            ''+''+
            ''+''+'510. Yellow Fever caused by. Answer: Female Mosquitoes  . Question'+
            ''+''+
            ''+''+'511. Who won more grand slams in the year 2015. Answer: Novak Djokovic  . Question'+
            ''+''+
            ''+''+'512. 2015 Arjuna Award given to which female wrestler. Answer: Babita Kumari  . Question'+
            ''+''+
            ''+''+'513. Full Form of RBC. Answer: Red Blood Cells  . Question'+
            ''+''+
            ''+''+'514. Afghanistan-s Parliament name is. Answer: Shora  . Question'+
            ''+''+
            ''+''+'515. Which is the Largest Stadium of America. Answer: Michigan Stadium  . Question'+
            ''+''+
            ''+''+'516. Nagaland capital. Answer: Kohima  . Question'+
            ''+''+
            ''+''+'517. NASA Headquarters. Answer: Washington DC  . Question'+
            ''+''+
            ''+''+'518. Stainless steel is. Answer: an alloy  . Question'+
            ''+''+
            ''+''+'519. Gun powder consists of. Answer: potassium nitrate  . Question'+
            ''+''+
            ''+''+'520. When did the british raj start in India. Answer: 1858  . Question'+
            ''+''+
            ''+''+'521. Infrared rays are. Answer:  electromagnetic waves.  . Question'+
            ''+''+
            ''+''+'522. Tashkent agreement signed after which Indo-Pak war. Answer: 1965  . Question'+
            ''+''+
            ''+''+'523. The length of digestive system. Answer: 30 Feet  . Question'+
            ''+''+
            ''+''+'524. Where is the statue of liberty. Answer: New York, USA  . Question'+
            ''+''+
            ''+''+'525. Maximum no of Medals in 2012 Olympics. Answer: USA  . Question'+
            ''+''+
            ''+''+'526. Winner of U19 World Cup . Answer: West Indies  . Question'+
            ''+''+
            ''+''+'527. Which cricketer hit consecutive three centuries in world cup cricket. Answer: Kumar Sangakkara  . Question'+
            ''+''+
            ''+''+'528. Khajuraho temples located in . Answer: MP  . Question'+
            ''+''+
            ''+''+'529. Which gas is released during respiration by human beings. Answer: carbon dioxide  . Question'+
            ''+''+
            ''+''+'530. State shares boundary with Bangladesh. Answer: Tripura  . Question'+
            ''+''+
            ''+''+'531. National sports day . Answer: August 29  . Question'+
            ''+''+
            ''+''+'532. Full Form of PDF . Answer: Portable Document Format  . Question'+
            ''+''+
            ''+''+'533. Man of the tournament 2011 world cup . Answer: Yuvraj Singh  . Question'+
            ''+''+
            ''+''+'534. Indian origin person gets Knighthood from Elizabeth II . Answer: Harpal Singh Kumaran  . Question'+
            ''+''+
            ''+''+'535. Capital of Dadra & Nagar Haveli. Answer: Silvassa  . Question'+
            ''+''+
            ''+''+'536. Language of Mughal Empire . Answer: Persian  . Question'+
            ''+''+
            ''+''+'537. Pitchblende is related to . Answer: Uranium  . Question'+
            ''+''+
            ''+''+'538. Who is author of Amar Sonar Bangla(National Anthem of Bangladesh). Answer: Rabindranath Tagore  . Question'+
            ''+''+
            ''+''+'539. Flag code of India. Answer: 2002  . Question'+
            ''+''+
            ''+''+'540. City on bank of Nile river. Answer: Khartoum  . Question'+
            ''+''+
            ''+''+'541. What is atomic number. Answer: The number of protons or electrons normally found in an atom of a given chemical elemen  . Question'+
            ''+''+
            ''+''+'542. which union territory is considered as smart city. Answer: New Delhi  . Question'+
            ''+''+
            ''+''+'543. Epidemiology is study of. Answer: the distribution and determinants of health-related states or events in specified populations  . Question'+
            ''+''+
            ''+''+'544. 1024GB . Answer: 1TB  . Question'+
            ''+''+
            ''+''+'545. What is biodiversity. Answer: Variety of life  . Question'+
            ''+''+
            ''+''+'546. Element responsible for air pollution. Answer: sulphur dioxide  . Question'+
            ''+''+
            ''+''+'547. The largest coal deposit in India . Answer: Damodar valley  . Question'+
            ''+''+
            ''+''+'548. Literacy rate of India as per 2011 census. Answer: 04%  . Question'+
            ''+''+
            ''+''+'549. The Biography of Indira Gandhi written by. Answer: Pupul Jayakar  . Question'+
            ''+''+
            ''+''+'550. Function of Hydrometer. Answer: measures the specific gravity (relative density) of liquids  . Question'+
            ''+''+
            ''+''+'551. Panipat Refinery belongs to. Answer: Haryana (IOCL)  . Question'+
            ''+''+
            ''+''+'552. Dadabhai Naoroji worked as a professor in which University. Answer: Elphinstone College  . Question'+
            ''+''+
            ''+''+'553. Indo-Pak war in which year. Answer: 1971  . Question'+
            ''+''+
            ''+''+'554. Which is most populous state according to 2011 census. Answer: Uttar Pradesh  . Question'+
            ''+''+
            ''+''+'555. Forest cover of India according to 2015 survey. Answer: 7,01,673 sq km  . Question'+
            ''+''+
            ''+''+'556. How many world heritage site in India by UNESCO. Answer: 32  . Question'+
            ''+''+
            ''+''+'557. In Computer, Which change source code into object code. Answer: Assembler  . Question'+
            ''+''+
            ''+''+'558. Which is not related to genetic engineering. Answer:  . Question'+
            ''+''+
            ''+''+'559. What is the National Game of USA. Answer: Baseball  . Question'+
            ''+''+
            ''+''+'560. Law of Inertia was given by. Answer: Newton  . Question'+
            ''+''+
            ''+''+'561. How many medals India gets in 12th South Asian Game. Answer: 188  . Question'+
            ''+''+
            ''+''+'562. Bio Diesel Locomotive Coming in which Railway Zone. Answer: Hubli Division  . Question'+
            ''+''+
            ''+''+'563. Which of the following is not a programming language. Answer: Assembly Language  . Question'+
            ''+''+
            ''+''+'564. Rank of India in Human Development Index. Answer: 130  . Question'+
            ''+''+
            ''+''+'565. What is the full form of ISI. Answer: Inter Services Intelligence  . Question'+
            ''+''+
            ''+''+'566. Vasco D gama reached first at which place in India. Answer: Kappad, Kerala  . Question'+
            ''+''+
            ''+''+'567. Tawang Monastery, in the Indian state of. Answer: Arunachal Pradesh  . Question'+
            ''+''+
            ''+''+'568. Anti-leprosy day. Answer: 30 January  . Question'+
            ''+''+
            ''+''+'569. Which soldier died on Feb 2016 in Siachen in J&K. Answer: Hanumanthappa Koppad  . Question'+
            ''+''+
            ''+''+'570. Alfred nobel discovered. Answer: Dynamite  . Question'+
            ''+''+
            ''+''+'571. Taj Mahal commissioned by . Answer: Mughal emperor Shah Jahan  . Question'+
            ''+''+
            ''+''+'572. Acid found in Grapes . Answer: Tartari  . Question'+
            ''+''+
            ''+''+'573. How many Muscles are used for eye ball. Answer: Six  . Question'+
            ''+''+
            ''+''+'574. How many number of players in POLO game. Answer: 4  . Question'+
            ''+''+
            ''+''+'575. First woman Doctor in the world. Answer: Elizabeth Blackwell  . Question'+
            ''+''+
            ''+''+'576. What is the nearest Galaxy to Milky Way. Answer: Andromeda galaxy  . Question'+
            ''+''+
            ''+''+'577. Who build Janther Manther in New Delhi. Answer: Maharaja Jai Singh II  . Question'+
            ''+''+
            ''+''+'578. National game of China . Answer: Table Tennis  . Question'+
            ''+''+
            ''+''+'579. Why plant leaves are in green colour. Answer: Chlorophy  . Question'+
            ''+''+
            ''+''+'580. South Africa Currency . Answer: South African rand  . Question'+
            ''+''+
            ''+''+'581. Zika virus is spreading by. Answer: Aedes Mosquito  . Question'+
            ''+''+
            ''+''+'582. IPTL stands for. Answer: International Premier tennis league  . Question'+
            ''+''+
            ''+''+'583. Where is valley international park located. Answer: USA  . Question'+
            ''+''+
            ''+''+'584. What is reason behind yellow colour of Papaya. Answer: Flavonoids  . Question'+
            ''+''+
            ''+''+'585. Who is founder of servant of Indian society. Answer: Gopal Krishna Gokhale  . Question'+
            ''+''+
            ''+''+'586. UPS stands for. Answer: Uninterrupted power supply  . Question'+
            ''+''+
            ''+''+'587. For which effect Einstein got nobel prize. Answer: Law of Photoelectric effect  . Question'+
            ''+''+
            ''+''+'588. Importance behind gov of India act 1935. Answer: Main source of Indian constitution  . Question'+
            ''+''+
            ''+''+'589. Main source of Vitamin-A. Answer: carrots  . Question'+
            ''+''+
            ''+''+'590. Indian institute of vegetable research is at. Answer: Varanasi  . Question'+
            ''+''+
            ''+''+'591. Valley of flowers in which state. Answer: uttarakhand  . Question'+
            ''+''+
            ''+''+'592. 11th Pakistan PM. Answer: Benazir Bhutto  . Question'+
            ''+''+
            ''+''+'593. World bank given money in December. Answer: Swacch bharat mission  . Question'+
            ''+''+
            ''+''+'594. Shape milky way galaxy. Answer: spiral  . Question'+
            ''+''+
            ''+''+'595. Gold medal boxer in asia. Answer: Mary Kom  . Question'+
            ''+''+
            ''+''+'596. Which country invented pencil. Answer: England  . Question'+
            ''+''+
            ''+''+'597. Stand up mission aim. Answer: Women and SC/ST empowerment  . Question'+
            ''+''+
            ''+''+'598. Bihu, celebrated in. Answer: Assam  . Question'+
            ''+''+
            ''+''+'599. Oxygen in photosynthesis is formed from. Answer: Water/CO2  . Question'+
            ''+''+
            ''+''+'600. Plasi war took place on which river. Answer: Bhagirathi river  . Question'+
            ''+''+
            ''+''+'601. 1stS president to attend republic day parade in India. Answer: Bill Clinton  . Question'+
            ''+''+
            ''+''+'602. Einstein got the Nobel prize for his theory of. Answer: Law of photoelectric effect  . Question'+
            ''+''+
            ''+''+'603. yellow color of papaya is due to the presence of. Answer: Carotene  . Question'+
            ''+''+
            ''+''+'604. In the rebellion of 1857, max. number of soldiers were in. Answer: Awadh  . Question'+
            ''+''+
            ''+''+'605. What does DNA Stands for in Biology. Answer: DEOXYRIBONUCLEIC Acid  . Question'+
            ''+''+
            ''+''+'606. NASA, the US space agency is planning to move from earth orbit to space area surrounding CISLUNAR Space. Answer: National Aeronautics and Space Administration  . Question'+
            ''+''+
            ''+''+'607. In September 2015 NASA scientists found evidence of flowing water on which planet outside Earth. Answer: Mars  . Question'+
            ''+''+
            ''+''+'608. What was the first football player from the Indian Sub continent to play for a European Club. Answer: Mohammed Saleem  . Question'+
            ''+''+
            ''+''+'609. What is the name of the parent company of Google, formed on 2nd October 2015. Answer: ALPHABET INC  . Question'+
            ''+''+
            ''+''+'610. Name India-s First Satellite. Answer: AryaBhatta  . Question'+
            ''+''+
            ''+''+'611. Who was named as the cultural ambassador of Seychelles in October 2015. Answer: AR Rahman  . Question'+
            ''+''+
            ''+''+'612. Which year was the economic liberalization in India Initiated. Answer: 1991  . Question'+
            ''+''+
            ''+''+'613. Which two Indian cities, were added to the creative city network of UNESCO in Dec 2015. Answer: Varanasi, Jaipur  . Question'+
            ''+''+
            ''+''+'614. Thermostat is a device in ovens which helps to maintain a temperature by. Answer: Regulating flow of heat  . Question'+
            ''+''+
            ''+''+'615. Who was the Confucius. Answer: Chinese Philosopher  . Question'+
            ''+''+
            ''+''+'616. Who is PV Sindhu. Answer: Badminton Player  . Question'+
            ''+''+
            ''+''+'617. Galvanization is a process in which a layer of zinc is put on iron objects to prevent them from. Answer: Rust  . Question'+
            ''+''+
            ''+''+'618. What do the terms Geocentric and Heliocentric refer to. Answer: Earth centered, Sun centered  . Question'+
            ''+''+
            ''+''+'619. What did Dmitri mendeleev formulate. Answer: Periodic Table  . Question'+
            ''+''+
            ''+''+'620. What is Electron. Answer: negative  . Question'+
            ''+''+
            ''+''+'621. In July 1905, who ordered the partition of Bengal. Answer: Lord Curzon  . Question'+
            ''+''+
            ''+''+'622. Kangchenjunga is. Answer: Himalayas  . Question'+
            ''+''+
            ''+''+'623. The purple frontier, the Earth dragon and the outer fortresses, all refer to. Answer: Great wall of china  . Question'+
            ''+''+
            ''+''+'624. Who was charles correa. Answer: Architect  . Question'+
            ''+''+
            ''+''+'625. Which of the following names is Nilanjana sudeshna, an Indian American Author popularly known as. Answer: Jhumpa Lahiri  . Question'+
            ''+''+
            ''+''+'626. What is the name of the Tablet computer produced by Datawind which is promoted by. Answer: Aakash a.k.a. Ubislate 7+ . Question'+
            ''+''+
            ''+''+'the GOVT of India as part of an e-learning program. Answer: Aakash  . Question'+
            ''+''+
            ''+''+'627. Who replaced viscount Louis Mountbatten as the governor general of Indian. Answer: C. Rajagopalachari  . Question'+
            ''+''+
            ''+''+'628. What is the Laccadive Sea otherwise known as. Answer: Arabian Sea  . Question'+
            ''+''+
            ''+''+'629. What is the unit of length used in formally to express astronomical distances. Answer: AU  . Question'+
            ''+''+
            ''+''+'630. Sajan Prakash related to. Answer: Swimming  . Question'+
            ''+''+
            ''+''+'631. First Nobel prize for medicine was given for which disease. Answer: Diphtheria  . Question'+
            ''+''+
            ''+''+'632. Capital City of Meghalaya. Answer: Shillong  . Question'+
            ''+''+
            ''+''+'633. Subhash Ghosh related to. Answer: Music  . Question'+
            ''+''+
            ''+''+'634. Alfred Nobel invented. Answer: Dynamite  . Question'+
            ''+''+
            ''+''+'635. 2015 Rugby Winner . Answer: New Zealand  . Question'+
            ''+''+
            ''+''+'636. Founder of Azad Hind Fauj(Indian Army). Answer: Subash Chandra Bose  . Question'+
            ''+''+
            ''+''+'637. Who invented WWW. Answer: Tim Berners Lee  . Question'+
            ''+''+
            ''+''+'638. What is the main element of Marsh gas. Answer: Methane  . Question'+
            ''+''+
            ''+''+'639. Who won Davis cup 2015. Answer: UK  . Question'+
            ''+''+
            ''+''+'640. When was Indian National Congress(INC) formed. Answer: December 28, 1885  . Question'+
            ''+''+
            ''+''+'641. Who founded North Korea. Answer: Kim II. Answer: Sung  . Question'+
            ''+''+
            ''+''+'642. Fatehpur sikri was founded by the Emperor. Answer: Akbar  . Question'+
            ''+''+
            ''+''+'643. What is the average thickness of skin. Answer:  . Question'+
            ''+''+
            ''+''+'644. In which state ONGC got environment free certificate for oil production. Answer: Andhra Pradesh  . Question'+
            ''+''+
            ''+''+'645. Which of the following is not Jupiter-s moon. Answer: Titan  . Question'+
            ''+''+
            ''+''+'646. 1. Bhutan official language . Answer: Dzongkha  . Question'+
            ''+''+
            ''+''+'647. When did the portuguese first arrived in India. Answer:  . Question'+
            ''+''+
            ''+''+'648. Change of position with respect to time . Answer: Velocity  . Question'+
            ''+''+
            ''+''+'649. What is Limerick. Answer: A limerick is a form of poetry, especially one in five-line.  . Question'+
            ''+''+
            ''+''+'650. Oneirology . Answer: Study of dreams  . Question'+
            ''+''+
            ''+''+'651. WLAN stands for . Answer: Wireless Local Area Network  . Question'+
            ''+''+
            ''+''+'652. PNR . Answer: Passenger Name Record  . Question'+
            ''+''+
            ''+''+'653. Anant Pai was . Answer: popularly known as Uncle Pai, was an Indian educationalist and a pioneer in Indian comics  . Question'+
            ''+''+
            ''+''+'654. India-s first child surgeon . Answer: Akrit jaswal (7 years old)  . Question'+
            ''+''+
            ''+''+'655. Freshwater lake . Answer: Wular Lake in J&K  . Question'+
            ''+''+
            ''+''+'656. Adhai din ka jhopra is built at . Answer: Ajmer (Rajasthan)  . Question'+
            ''+''+
            ''+''+'657. LIGO . Answer: Laser Interferometer Gravitational wave observatory  . Question'+
            ''+''+
            ''+''+'658. What is logo of Make in India. Answer: Moving Lion  . Question'+
            ''+''+
            ''+''+'659. +91 code is which country. Answer: India  . Question'+
            ''+''+
            ''+''+'660. C6H6 . Answer: Benzene  . Question'+
            ''+''+
            ''+''+'661. 1st olympic game held at . Answer: Athens  . Question'+
            ''+''+
            ''+''+'662. Malgudi days was written by. Answer: R. Narayan  . Question'+
            ''+''+
            ''+''+'663. What is Shinjo. Answer: A city in Japan  . Question'+
            ''+''+
            ''+''+'664. When a gravitational force is exerted on a mass object then it is called. Answer:  . Question'+
            ''+''+
            ''+''+'665. Shigmo. Answer: a spring festival celebrated in Goa  . Question'+
            ''+''+
            ''+''+'666. BESK Stands for . Answer: Binary electronic sequence calculator  . Question'+
            ''+''+
            ''+''+'667. In which year Sikkim state was formed. Answer: 1975  . Question'+
            ''+''+
            ''+''+'668. Which is most abundant natural combustible gas-Methane  . Question'+
            ''+''+
            ''+''+'669. PM of Pakistan in 1999. Answer: Nawaz sharif  . Question'+
            ''+''+
            ''+''+'670. Headquarters of UNO-New york  . Question'+
            ''+''+
            ''+''+'671. "In the practice of tolerance, one-s enemy is the best teacher" is quoted by. Answer: Dalai Lama  . Question'+
            ''+''+
            ''+''+'672. In which year Arunachal Pradesh state is formed. Answer: 1972  . Question'+
            ''+''+
            ''+''+'673. Uganda capital . Answer: Kampala  . Question'+
            ''+''+
            ''+''+'674. Country got independence in 2011. Answer: South Sudan  . Question'+
            ''+''+
            ''+''+'675. Cultivation of saffron. Answer: Kashmir(in India), Iran (world)  . Question'+
            ''+''+
            ''+''+'676. Women participated all events in which Olympics. Answer: 1900 Games in Paris  . Question'+
            ''+''+
            ''+''+'677. Parliament in Delhi constructed by. Answer: Edwin Lutyens, Herbert Baker  . Question'+
            ''+''+
            ''+''+'678. Borrowed emergency provision from which country. Answer: Germany  . Question'+
            ''+''+
            ''+''+'679. Sri Lanka got independence in which year. Answer: 4th Feb,1948  . Question'+
            ''+''+
            ''+''+'680. Age limit of pm. Answer: No upper limit, min. 25 years  . Question'+
            ''+''+
            ''+''+'681. Ashoka from which dynasty. Answer: Mauryan dynasty  . Question'+
            ''+''+
            ''+''+'682. Scientific name of Human Beings. Answer: Homo sapiens  . Question'+
            ''+''+
            ''+''+'683. Recently creature which lives without water for 10 yrs. Answer: Tardigrade  . Question'+
            ''+''+
            ''+''+'684. Korea currency. Answer: South Korean won  . Question'+
            ''+''+
            ''+''+'685. Gujarat capital. Answer: Gandhinagar  . Question'+
            ''+''+
            ''+''+'686. First man to reach outer space. Answer: Yuri Gagarin ( Russian Cosmonaut)  . Question'+
            ''+''+
            ''+''+'687. Nacl means like salt/water/sugar. Answer: Salt  . Question'+
            ''+''+
            ''+''+'688. Periodic table invented by. Answer: Dmitri Mendeleev  . Question'+
            ''+''+
            ''+''+'689. X rays invented by. Answer: Roentgen  . Question'+
            ''+''+
            ''+''+'690. Fastest acting anti rabies vaccine developed country. Answer: India  . Question'+
            ''+''+
            ''+''+'691. Fundamental duties taken from which country . Answer: USSR  . Question'+
            ''+''+
            ''+''+'692. World Economic Forum 2015 meeting held at. Answer: Switzerland  . Question'+
            ''+''+
            ''+''+'693. In which game women first compete in the Olympic Game. Answer:  . Question'+
            ''+''+
            ''+''+'694. Ellora caves in which state. Answer: Maharashtra  . Question'+
            ''+''+
            ''+''+'695. 100 year war between which two countries. Answer: France and England  . Question'+
            ''+''+
            ''+''+'696. Mrinalini sarabhai is famous for. Answer: Indian Classical Dancer  . Question'+
            ''+''+
            ''+''+'697. The last ruler of maurya dynasty. Answer: Brihadratha Maurya  . Question'+
            ''+''+
            ''+''+'698. Manohar Parrikar hoists country-s largest, tallest tricolour at Ranchi  . Question'+
            ''+''+
            ''+''+'699. The presence of which gases in air makes brass discoloured. Answer: Hydrogen sulphide  . Question'+
            ''+''+
            ''+''+'700. Highest cricket ground in India in which state. Answer: Chail, Himachal Pradesh  . Question'+
            ''+''+
            ''+''+'701. What is Geotropism. Answer: The growth of the parts of plants in response to the force of gravity  . Question'+
            ''+''+
            ''+''+'702. India:Tiger::USA:. Answer: Bald Eagle  . Question'+
            ''+''+
            ''+''+'703. What is the colour of Solid Iodine. Answer: purple  . Question'+
            ''+''+
            ''+''+'704. Inventor of Email . Answer: Shiva Ayyadurai  . Question'+
            ''+''+
            ''+''+'705. India-s 5th navigational satellites name. Answer: PSLV-C31  . Question'+
            ''+''+
            ''+''+'706. Who invented dynamo. Answer: Michael Faraday  . Question'+
            ''+''+
            ''+''+'707. If pH value becomes less than 7 then it is called as. Answer: Acidic  . Question'+
            ''+''+
            ''+''+'708. Nephrology is the study of. Answer: Kidney function  . Question'+
            ''+''+
            ''+''+'709. First indian to get nobel prize. Answer: Rabindranath Tagore  . Question'+
            ''+''+
            ''+''+'710. In the first ODI match of INDIA ,who is captain. Answer: Ajit Wadekar  . Question'+
            ''+''+
            ''+''+'711. The words "Satyameva Jayate" taken from . Answer: Mundaka Upanishad  . Question'+
            ''+''+
            ''+''+'712. Basilica of bom jesus is located at. Answer: Goa  . Question'+
            ''+''+
            ''+''+'713. Jayakwadi dam located on which river. Answer: Godavari  . Question'+
            ''+''+
            ''+''+'714. Oldest oil reserves in India. Answer: Digboi  . Question'+
            ''+''+
            ''+''+'715. What is tri colour ratio of Indian National Flag. Answer: Width : Length = 2:3  . Question'+
            ''+''+
            ''+''+'716. National song of India was composed by. Answer: Bankim Chandra Chatterjee  . Question'+
            ''+''+
            ''+''+'717. Kidney stone is caused by. Answer: Calcium Oxalate  . Question'+
            ''+''+
            ''+''+'718. Dog : Kernel :: Bee : . Answer: Beehive  . Question'+
            ''+''+
            ''+''+'719. How many tastes buds are present in tongue. Answer: 5  . Question'+
            ''+''+
            ''+''+'720. On which planet frozen water is found. Answer: Pluto  . Question'+
            ''+''+
            ''+''+'721. Tennis is played on which surface. Answer: Hard, Grass and Clay courts  . Question'+
            ''+''+
            ''+''+'722. How many bones a Infant baby have. Answer: 300  . Question'+
            ''+''+
            ''+''+'723. White desert in India. Answer: Rann of Kutch desert  . Question'+
            ''+''+
            ''+''+'724. Which thing was discovered by Alexander Fleming. Answer: Penicillin  . Question'+
            ''+''+
            ''+''+'725. Mughal dynasty was established by. Answer: Babur  . Question'+
            ''+''+
            ''+''+'726. Which of following colour has least wavelength. Answer: Violet  . Question'+
            ''+''+
            ''+''+'727. First woman President of Pakistan. Answer: Dr. Fehmida Mirza  . Question'+
            ''+''+
            ''+''+'728. Which was first geostationary satellite launched in India. Answer: Ariane Passenger Payload Experiment  . Question'+
            ''+''+
            ''+''+'729. Father of Indian Space Programmes. Answer: Dr Vikram Sarabhai  . Question'+
            ''+''+
            ''+''+'730. First President of Indian National Congress. Answer: W.C. Banerjee  . Question'+
            ''+''+
            ''+''+'731. Nobel prize recipient of India in 2014 for peace. Answer: Kailash Satyarthi  . Question'+
            ''+''+
            ''+''+'732. Height of badminton net above ground level. Answer: 524 meter  . Question'+
            ''+''+
            ''+''+'733. World-s first space tourist. Answer: Dennis Tito  . Question'+
            ''+''+
            ''+''+'734. Who introduced Orthodox Christianity in Russia. Answer: Vladimir  . Question'+
            ''+''+
            ''+''+'735. Which of following element is found in room temperature. Answer: Bromine  . Question'+
            ''+''+
            ''+''+'736. Molecular formula for sugar. Answer: C12H22O11  . Question'+
            ''+''+
            ''+''+'737. Which monument was built to commemorate the eradication of plague. Answer: Charminar  . Question'+
            ''+''+
            ''+''+'738. Air conditioner was invented by. Answer: Willis Carrier  . Question'+
            ''+''+
            ''+''+'739. PM born after Independence . Answer: Narendra Modi  . Question'+
            ''+''+
            ''+''+'740. What is English IVY . Answer: Flower  . Question'+
            ''+''+
            ''+''+'741. What is Guru Shikhar . Answer: a peak in the Arbuda Mountains of Rajasthan  . Question'+
            ''+''+
            ''+''+'742. Mycology. Answer: Study of fungi  . Question'+
            ''+''+
            ''+''+'743. "Live as if you were to die tomorrow". Answer: Mahatma Gandhi  . Question'+
            ''+''+
            ''+''+'744. "Life On My Terms: From the Grassroots to the Corridors of Power" is an autobiography of. Answer: Sharad Pawar  . Question'+
            ''+''+
            ''+''+'745. Who is Chanda Kochhar . Answer: MD & CEO Of ICICI bank  . Question'+
            ''+''+
            ''+''+'746. Language spoken in Tamil Nadu and Sri Lanka. Answer: Tamil  . Question'+
            ''+''+
            ''+''+'747. Who discovered penicillin . Answer: Alexander Fleming  . Question'+
            ''+''+
            ''+''+'748. Indian village where people speak in Sanskrit . Answer: Mattur  . Question'+
            ''+''+
            ''+''+'749. Zika Virus caused by. Answer: Aedes mosquitoes  . Question'+
            ''+''+
            ''+''+'750. When Virat Kohli given Arjuna Award. Answer: 2013  . Question'+
            ''+''+
            ''+''+'751. Exobiology. Answer: deals with the search for extraterrestrial life  . Question'+
            ''+''+
            ''+''+'752. Person can see only nearby objects. Answer: Myopia  . Question'+
            ''+''+
            ''+''+'753. Prostate is a. Answer: Gland  . Question'+
            ''+''+
            ''+''+'754. Bangladesh got its constitution on. Answer: November 4, 1972  . Question'+
            ''+''+
            ''+''+'755. Players in each side of volleyball. Answer: 6  . Question'+
            ''+''+
            ''+''+'756. Legislative powers vested with whom. Answer: Parliament of India  . Question'+
            ''+''+
            ''+''+'757. AC TO DC is converted by. Answer: Rectifier  . Question'+
            ''+''+
            ''+''+'758. Triratna is related to. Answer: Buddhism or Jainism  . Question'+
            ''+''+
            ''+''+'759. Grand slam is combination of. Answer: AUS Open, French Open, US open and Wimbledon  . Question'+
            ''+''+
            ''+''+'760. Which of these is not book by Abdul kalam. Answer: My Country My Life  . Question'+
            ''+''+
            ''+''+'761. Kalpana chawla Space shuttle name. Answer: Columbia  . Question'+
            ''+''+
            ''+''+'762. Hirakud is located on bank of river. Answer: Mahanandi  . Question'+
            ''+''+
            ''+''+'763. In LAL-BAL-PAL, who are BAL AND LAL. Answer: Bal Gangadhar Tilak and Lala Lajpat rai  . Question'+
            ''+''+
            ''+''+'764. Which authority is elected on the basis of proportional representation. Answer: President  . Question'+
            ''+''+
            ''+''+'765. Kurukshetra is near to which city. Answer: Ambala  . Question'+
            ''+''+
            ''+''+'766. Crop insurance scheme. Answer: PMFBY  . Question'+
            ''+''+
            ''+''+'767. IMO full form. Answer: International Maritime Organisation  . Question'+
            ''+''+
            ''+''+'768. 1st home minister. Answer: Vallabhbhai Patel  . Question'+
            ''+''+
            ''+''+'769. National unity day. Answer: October 31  . Question'+
            ''+''+
            ''+''+'770. NASA situated in. Answer: Washington C.  . Question'+
            ''+''+
            ''+''+'771. Gandhi. Answer: Irvin Pact signed on. Answer: 5th March 1931  . Question'+
            ''+''+
            ''+''+'772. Headquarters of ISRO. Answer: Bengaluru  . Question'+
            ''+''+
            ''+''+'773. Percentage of Nitrogen in weather. Answer: 76%  . Question'+
            ''+''+
            ''+''+'774. Sachin played his first test match in 1989 against which country. Answer: Pakistan  . Question'+
            ''+''+
            ''+''+'775. First Bank In India was. Answer: Bank of Hindustan  . Question'+
            ''+''+
            ''+''+'776. First Olympic Games In Which Country. Answer: Athens, Greece  . Question'+
            ''+''+
            ''+''+'777. Google CEO is. Answer: Sundar Pichai  . Question'+
            ''+''+
            ''+''+'778. Cheque Validity remains for. Answer: 3 Months  . Question'+
            ''+''+
            ''+''+'779. National Science Day. Answer: Feb 28  . Question'+
            ''+''+
            ''+''+'780. First Deputy Prime Minister. Answer: Sardar Vallabhai Patel  . Question'+
            ''+''+
            ''+''+'781. Shimla Agreement in which place and year. Answer: Simla in 1972  . Question'+
            ''+''+
            ''+''+'782. J&K East boundary. Answer: LOC  . Question'+
            ''+''+
            ''+''+'783. After 9/11 Tragedy world Trade center new name. Answer: One World Trade Center  . Question'+
            ''+''+
            ''+''+'784. Shortcut for expand browsing screen in web browser(F1/F11/F10/F4). Answer: F11  . Question'+
            ''+''+
            ''+''+'785. 2023 cricket world cup Hosting Country. Answer: India  . Question'+
            ''+''+
            ''+''+'786. Rupee Symbol in which language. Answer: Devanagari  . Question'+
            ''+''+
            ''+''+'787. Paracetamol is . Answer: Analgesic  . Question'+
            ''+''+
            ''+''+'788. Ganga action plan to. Answer: To Purify Ganga River  . Question'+
            ''+''+
            ''+''+'789. ASCII stands for. Answer: American Standard Code for Information Interchange  . Question'+
            ''+''+
            ''+''+'790. Chicken pox virus. Answer: varicella zoster virus (VZV)  . Question'+
            ''+''+
            ''+''+'791. Commonwealth game first time in India in which year. Answer: 2010  . Question'+
            ''+''+
            ''+''+'792. India and which country agreement for solar power. Answer:  . Question'+
            ''+''+
            ''+''+'793. Date to change Pre 2005 notes. Answer: June 30, 2016  . Question'+
            ''+''+
            ''+''+'794. 1 rupee note bears signature of. Answer: Finance Secretary  . Question'+
            ''+''+
            ''+''+'795. First women President of congress. Answer: Annie Besant  . Question'+
            ''+''+
            ''+''+'796. Chemotherapy is used for treatment of. Answer: Cancer  . Question'+
            ''+''+
            ''+''+'797. First women to win gold medal in boxing. Answer: Nicola Adams  . Question'+
            ''+''+
            ''+''+'798. Arunachal Pradesh capital. Answer: Itanagar  . Question'+
            ''+''+
            ''+''+'799. Jallikattu game played in which state. Answer: Tamil Nadu  . Question'+
            ''+''+
            ''+''+'800. 15th PM of India. Answer: Narendra Modi  . Question'+
            ''+''+
            ''+''+'801. MS Office is. Answer: Application software  . Question'+
            ''+''+
            ''+''+'802. Ganga of South India is. Answer: Godavari  . Question'+
            ''+''+
            ''+''+'803. Bhagat Singh executed in which year. Answer: 1931  . Question'+
            ''+''+
            ''+''+'804. Computer shortcut key to get help menu. Answer: F1  . Question'+
            ''+''+
            ''+''+'805. LOC between India and Pakistan was constructed in. Answer: 1972  . Question'+
            ''+''+
            ''+''+'806. National flag of India was designed by. Answer: Pingali Venkayya  . Question'+
            ''+''+
            ''+''+'807. Which states achieved 100% inclusion in PMJDY. Answer: Goa and Kerala  . Question'+
            ''+''+
            ''+''+'808. How many languages on Indian notes. Answer: 17  . Question'+
            ''+''+
            ''+''+'809. Author of Wings of Fire. Answer: Dr P.J. Abdul Kalam  . Question'+
            ''+''+
            ''+''+'810. Who invented Audio Phones. Answer: Nathaniel Baldwin  . Question'+
            ''+''+
            ''+''+'811. Which one is not search engine. Answer: Flipkart  . Question'+
            ''+''+
            ''+''+'812. How much decibel can a human ear hear. Answer: 60-120 DB  . Question'+
            ''+''+
            ''+''+'813. Which pm-s name could b seen on indian currency notes. Answer: Manmohan Singh  . Question'+
            ''+''+
            ''+''+'814. Capital of J&K in summer. Answer: Srinagar  . Question'+
            ''+''+
            ''+''+'815. Full form of IFSC. Answer: Indian Financial System Code  . Question'+
            ''+''+
            ''+''+'816. Quit India was held in which year. Answer: 1942  . Question'+
            ''+''+
            ''+''+'817. Thar desert is in. Answer: Rajasthan  . Question'+
            ''+''+
            ''+''+'818. Study of cancer. Answer: Oncology  . Question'+
            ''+''+
            ''+''+'819. Good governance day. Answer: 25 December  . Question'+
            ''+''+
            ''+''+'820. Constitution day. Answer: 26 November  . Question'+
            ''+''+
            ''+''+'821. Venue of cricket world cup 2019. Answer: England & Wales  . Question'+
            ''+''+
            ''+''+'822. Headquarter of UNO. Answer: New York  . Question'+
            ''+''+
            ''+''+'823. Shimla agreement between. Answer: Indira Gandhi and Z A Bhutto  . Question'+
            ''+''+
            ''+''+'824. Young india weekly Journal. Answer: Mahatma Gandhi  . Question'+
            ''+''+
            ''+''+'825. Money Transfer through mobile is called. Answer: IMPS  . Question'+
            ''+''+
            ''+''+'826. National Space Society headquarters. Answer: Washington C  . Question'+
            ''+''+
            ''+''+'827. From where we get Vitamin-D from given options. Answer: Cod Liver Oil  . Question'+
            ''+''+
            ''+''+'828. Normal eye vision distance. Answer: 6 meters  . Question'+
            ''+''+
            ''+''+'829. CK Naidu Lifetime Achievement award winner. Answer: Syed Kirmani  . Question'+
            ''+''+
            ''+''+'830. Which compound in LPG gives it smell on leakage. Answer: Ethyl Mercaptan  . Question'+
            ''+''+
            ''+''+'831. Yogini cult has its origin from which state. Answer: Odisha  . Question'+
            ''+''+
            ''+''+'832. Which freedom fighter introduced Western education. Answer: Raja Ram Mohan Roy  . Question'+
            ''+''+
            ''+''+'833. Rti implemented/adopted in which year. Answer: 2005  . Question'+
            ''+''+
            ''+''+'834. Second longest river of india. Answer: Godavari  . Question'+
            ''+''+
            ''+''+'835. India-s border is longest with which nation. Answer: Bangladesh  . Question'+
            ''+''+
            ''+''+'836. Who won 1st olympic medal of badminton. Answer: Saina Nehwal  . Question'+
            ''+''+
            ''+''+'837. Who among these did not get bharat ratna. Answer: AR Rahman  . Question'+
            ''+''+
            ''+''+'838. When did kailash satyarthi and malala got nobel peace prize. Answer: 2014  . Question'+
            ''+''+
            ''+''+'839. Which is not a greenhouse gas. Answer: Hydrogen  . Question'+
            ''+''+
            ''+''+'840. When was rupee symbol adopted. Answer: 2010  . Question'+
            ''+''+
            ''+''+'841. When did Indian mars mission start. Answer: Sep 24, 2014  . Question'+
            ''+''+
            ''+''+'842. Who was the 1st lady president of Indian National congress. Answer: Annie Besant  . Question'+
            ''+''+
            ''+''+'843. Where was national science conference held in India. Answer: New Delhi  . Question'+
            ''+''+
            ''+''+'844. Which of the following declared cow as personality of 2015. Answer: (google, microsoft, yahoo or facebook) Yahoo  . Question'+
            ''+''+
            ''+''+'845. Bismark of India. Answer: Sardar Vallabhbhai Patel  . Question'+
            ''+''+
            ''+''+'846. World heritage site Bhimbetka in Madhya Pradesh is famous for. Answer: Rock  . Question'+
            ''+''+
            ''+''+'847. Chief guest on republic day 2016. Answer: Francois Hollande  . Question'+
            ''+''+
            ''+''+'848. Osteoporosis is related to. Answer: Bone  . Question'+
            ''+''+
            ''+''+'849. If the Temperature of the body decreases this condition is called. Answer: Hypothalamus  . Question'+
            ''+''+
            ''+''+'850. Akash missile is. Answer: Surface to Air Missile  . Question'+
            ''+''+
            ''+''+'851. Suez Canal. Answer: Egypt  . Question'+
            ''+''+
            ''+''+'852. What is Graphene. Answer: a form of carbon  . Question'+
            ''+''+
            ''+''+'853. RADAR full form. Answer: RAdio Detection And Ranging  . Question'+
            ''+''+
            ''+''+'854. What is umami. Answer: Savory taste  . Question'+
            ''+''+
            ''+''+'855. Highest grand slams winner male. Answer: Roger Federer  . Question'+
            ''+''+
            ''+''+'856. Oscar winner director from India. Answer: Satyajit Ray  . Question'+
            ''+''+
            ''+''+'857. DPT Full Form. Answer: Diphtheria, Pertussis, Tetanus  . Question'+
            ''+''+
            ''+''+'858. Which river flows through Karnataka. Answer: Kaveri  . Question'+
            ''+''+
            ''+''+'859. 2015 TIME person of the year. Answer: Angela Merkel  . Question'+
            ''+''+
            ''+''+'860. Father of geometry. Answer: Euclid  . Question'+
            ''+''+
            ''+''+'861. Zika virus spread by. Answer: Aedes mosquitoes  . Question'+
            ''+''+
            ''+''+'862. Lemur are found in. Answer: Madagascar  . Question'+
            ''+''+
            ''+''+'863. Chemical name of Baking soda. Answer: Sodium Bicarbonate  . Question'+
            ''+''+
            ''+''+'864. What is tomato. Answer: fruit  . Question'+
            ''+''+
            ''+''+'865. Berlin wall demolished in which year. Answer: 1989  . Question'+
            ''+''+
            ''+''+'866. Which language use ideographs. Answer: China and Japan  . Question'+
            ''+''+
            ''+''+'867. SPM full form. Answer: Suspended Particulate Matter  . Question'+
            ''+''+
            ''+''+'868. Tallest building in world. Answer: Burj Khalifa  . Question'+
            ''+''+
            ''+''+'869. Who gives oath to the President. Answer: Chief Justice of India  . Question'+
            ''+''+
            ''+''+'870. Chief justice of India retirement age. Answer: 65 years  . Question'+
            ''+''+
            ''+''+'871. Chandrasekhar Limit is applied to. Answer: Mass  . Question'+
            ''+''+
            ''+''+'872. Kamarupa kingdom is in which state. Answer: Assam  . Question'+
            ''+''+
            ''+''+'873. Which indian king used naval power to conquer ports of east asia. Answer: rajendra chola  . Question'+
            ''+''+
            ''+''+'874. Where is the island of Seychelles located. Answer: Indian Ocean  . Question'+
            ''+''+
            ''+''+'875. Greenhouse gas effect on Earth. Answer: global warming  . Question'+
            ''+''+
            ''+''+'876. Land locked country. Answer:  . Question'+
            ''+''+
            ''+''+'877. Largest non polar desert in the world. Answer: Sahara  . Question'+
            ''+''+
            ''+''+'878. Where was paper invented. Answer: China  . Question'+
            ''+''+
            ''+''+'879. Who was the first to score a perfect 10 in olympics in Gymnastics. Answer: Nadia Elena  . Question'+
            ''+''+
            ''+''+'880. UNESCO headquarters. Answer: Paris  . Question'+
            ''+''+
            ''+''+'881. Thailand currency. Answer: Thai Baht  . Question'+
            ''+''+
            ''+''+'882. RBI founded in. Answer: 1935  . Question'+
            ''+''+
            ''+''+'883. Jimmy Wales and Larry Sanger related with which company. Answer: Wikipedia  . Question'+
            ''+''+
            ''+''+'884. What did Edward jenney pioneer . Answer:  . Question'+
            ''+''+
            ''+''+'885. Quit India Revolution. Answer: 8 August 1942  . Question'+
            ''+''+
            ''+''+'886. Interpol headquarter. Answer: Lyon, France  . Question'+
            ''+''+
            ''+''+'887. Environment day. Answer: 5 June  . Question'+
            ''+''+
            ''+''+'888. smallest bone in human body. Answer: stapes  . Question'+
            ''+''+
            ''+''+'889. subhash chandra bhose father-s name. Answer: Janakinath Bose  . Question'+
            ''+''+
            ''+''+'890. National song written by. Answer: Bankim Chandra Chattopadhyay  . Question'+
            ''+''+
            ''+''+'891. Where do u find Kunjilal waterfalls. Answer: Karnataka  . Question'+
            ''+''+
            ''+''+'892. Organ that can grow and regenerate. Answer: Liver  . Question'+
            ''+''+
            ''+''+'893. Last Mughal emperor. Answer: Bahadur Shah Zafar  . Question'+
            ''+''+
            ''+''+'894. Pollination by wind is called. Answer: Anemophily or wind pollination  . Question'+
            ''+''+
            ''+''+'895. Brightest star in our sky. Answer: Sirius A  . Question'+
            ''+''+
            ''+''+'896. Medieval indian book of mathematics . Answer: George Gheverghese Joseph  . Question'+
            ''+''+
            ''+''+'897. Mangalyan launched from. Answer: Sriharikota  . Question'+
            ''+''+
            ''+''+'898. A Deep crack in glacier is called. Answer: crevasse  . Question'+
            ''+''+
            ''+''+'899. Frontier Gandhi is. Answer: Khan Abdul gaffar khan  . Question'+
            ''+''+
            ''+''+'900. Which is Always present in organic compound. Answer: Carbon  . Question'+
            ''+''+
            ''+''+'901. Largest freshwater lake. Answer: Lake Baikal  . Question'+
            ''+''+
            ''+''+'902. Called Aurum . Answer: Bronze 2.Gold 3.Silver 4.Copper. Answer: Gold  . Question'+
            ''+''+
            ''+''+'903. Granite is an example of. Answer: Igneous  . Question'+
            ''+''+
            ''+''+'904. Din i ilahi founder. Answer: Akbar  . Question'+
            ''+''+
            ''+''+'905. Queensberry is associated to which sports. Answer: modern boxing  . Question'+
            ''+''+
            ''+''+'906. Which country max time won FIFA world cup. Answer: Brazil  . Question'+
            ''+''+
            ''+''+'907. Blood colour of octopus-Blue  . Question'+
            ''+''+
            ''+''+'908. Name of the father of subhas chandra bose . Answer: Janakinath Bose  . Question'+
            ''+''+
            ''+''+'909. New name of Bharatpur national park . Answer: Keoladeo National Park  . Question'+
            ''+''+
            ''+''+'910. Real is the currency of . Answer: Brazil  . Question'+
            ''+''+
            ''+''+'911. krishna river originated from which state. Answer: Maharashtra  . Question'+
            ''+''+
            ''+''+'912. LAN Fullform . Answer: Local Area Network  . Question'+
            ''+''+
            ''+''+'913. Evolution theory is given by . Answer: Darwin  . Question'+
            ''+''+
            ''+''+'914. First olympic medal winner . Answer: Norman Pritchard  . Question'+
            ''+''+
            ''+''+'915. First Dadasaheb Phalke Award winner . Answer: Devika Rani  . Question'+
            ''+''+
            ''+''+'916. Indian Institute of science located in . Answer: Karnataka  . Question'+
            ''+''+
            ''+''+'917. Thomas Cup related to . Answer: Badminton  . Question'+
            ''+''+
            ''+''+'918. Miss Universe 2015 . Answer: Pia Alonzo Wurtzbach  . Question'+
            ''+''+
            ''+''+'919. Other names of Chanakya . Answer: Vishnugupta, Kautilya  . Question'+
            ''+''+
            ''+''+'920. ONGC Headquarters. Answer: Uttarakhand  . Question'+
            ''+''+
            ''+''+'921. Which city of Australia have high population. Answer: Sydney  . Question'+
            ''+''+
            ''+''+'922. Titanic ship belongs to which country . Answer: UK  . Question'+
            ''+''+
            ''+''+'923. The Best animated film at Oscar. Answer: Inside Out  . Question'+
            ''+''+
            ''+''+'924. The bird which flies backward. Answer: Hummingbirds  . Question'+
            ''+''+
            ''+''+'925. Father of Jawaharlal Nehru . Answer: Motilal Nehru  . Question'+
            ''+''+
            ''+''+'926. Dronacharya Award(Boxing) 2016. Answer: Swatantra Raj Singh  . Question'+
            ''+''+
            ''+''+'927. Which river originates from western ghat. Answer: Kaveri  . Question'+
            ''+''+
            ''+''+'928. Energy of sun by which process. Answer: Nuclear fusion  . Question'+
            ''+''+
            ''+''+'929. Who invented brahmo samaj. Answer: Raja Ram Mohan Rai  . Question'+
            ''+''+
            ''+''+'930. Elephanta Caves Situated in . Answer: Raigad, Maharashtra  . Question'+
            ''+''+
            ''+''+'931. Biggest Mammal. Answer: Blue whale  . Question'+
            ''+''+
            ''+''+'932. Current Chief Justice India. Answer: T. S. Thakur  . Question'+
            ''+''+
            ''+''+'933. Earth-s water cycle powered by. Answer: Sun  . Question'+
            ''+''+
            ''+''+'934. Capital of Denmark. Answer: Copenhagen  . Question'+
            ''+''+
            ''+''+'935. International Yoga Day. Answer: June 21  . Question'+
            ''+''+
            ''+''+'936. Jan-4 Independence day of which country. Answer: Myanmar  . Question'+
            ''+''+
            ''+''+'937. winter session Olympic game venue. Answer: Pyeongchang, South Korea  . Question'+
            ''+''+
            ''+''+'938. Oldest dam of India. Answer: Kallanai Dam  . Question'+
            ''+''+
            ''+''+'939. of player in kho kho game. Answer: 9  . Question'+
            ''+''+
            ''+''+'940. First indian lady to won gold in asian game. Answer: Kamaljeet Sandhu  . Question'+
            ''+''+
            ''+''+'941. First hockey player to get padma shri. Answer: Dilip Tirkey  . Question'+
            ''+''+
            ''+''+'942. Second largest country in respect of land area. Answer: Canada  . Question'+
            ''+''+
            ''+''+'943. Reuters newspaper headquarter. Answer: London  . Question'+
            ''+''+
            ''+''+'944. of fundamental duties. Answer: 11  . Question'+
            ''+''+
            ''+''+'945. Winner of men-s french open 2015. Answer: Stan Wawrinka  . Question'+
            ''+''+
            ''+''+'946. UN climate change meeting held in which place. Answer: Paris  . Question'+
            ''+''+
            ''+''+'947. DMK party is founded by whom. Answer: C. Annadurai  . Question'+
            ''+''+
            ''+''+'948. Ethanol is obtained from which-(rice, sugarcane, sunflower, petrol). Answer: sugarcane  . Question'+
            ''+''+
            ''+''+'949. Ajanta and Ellora cave is located in which state. Answer: Maharashtra  . Question'+
            ''+''+
            ''+''+'950. Study of birds. Answer: Ornithology  . Question'+
            ''+''+
            ''+''+'951. Den is to lion, Aviary is to. Answer: Birds  . Question'+
            ''+''+
            ''+''+'952. Group of dolphin is called. Answer: school or a pod  . Question'+
            ''+''+
            ''+''+'953. Polio vaccine is developed by. Answer: Jonas Salk  . Question'+
            ''+''+
            ''+''+'954. Name of dog who first goes to space. Answer: Laika  . Question'+
            ''+''+
            ''+''+'955. Father of space research. Answer: Vikram Sarabhai  . Question'+
            ''+''+
            ''+''+'956. Smallest planet. Answer: Mercury  . Question'+
            ''+''+
            ''+''+'957. Buddha attained enlightenment at. Answer: Bodh Gaya  . Question'+
            ''+''+
            ''+''+'958. First governor general of free india. Answer: Lord Canning  . Question'+
            ''+''+
            ''+''+'959. Instrument to detect object under water. Answer: Sonar  . Question'+
            ''+''+
            ''+''+'960. First Lok sabha speaker. Answer: Ganesh Vasudev Mavalankar  . Question'+
            ''+''+
            ''+''+'961. Rowlatt act year. Answer: 1919  . Question'+
            ''+''+
            ''+''+'962. TB day observed on. Answer: March 24  . Question'+
            ''+''+
            ''+''+'963. Who gave the slogan "do or die". Answer: Mahatma Gandhi  . Question'+
            ''+''+
            ''+''+'964. When did Indian constitution came into amendment. Answer: 1951  . Question'+
            ''+''+
            ''+''+'965. What is the name of horse of Maharana Pratap. Answer: Chetak  . Question'+
            ''+''+
            ''+''+'966. Karnam Malleswari related to which game. Answer: Weightlifting  . Question'+
            ''+''+
            ''+''+'967. In which places dead bodies are not buried options out of given options. Answer:  . Question'+
            ''+''+
            ''+''+'968. First international cricket match was played between. Answer: USA and Canada  . Question'+
            ''+''+
            ''+''+'969. Golden temple of dambulla is present in. Answer: Sri Lanka  . Question'+
            ''+''+
            ''+''+'970. Cyprus capital. Answer: Nicosia  . Question'+
            ''+''+
            ''+''+'971. Sorrow of Bengal. Answer: Damodar River  . Question'+
            ''+''+
            ''+''+'972. First Satellite launched to Moon. Answer: Sputnik 1  . Question'+
            ''+''+
            ''+''+'973. Establishment of the panchayati Raj System was recommended by. Answer: Balwant Rai Mehta Committee Report 1957  . Question'+
            ''+''+
            ''+''+'974. By which Constitutional Amendment the voting age was reduced from 21 years to 18 years. Answer: 61 Amendment  . Question'+
            ''+''+
            ''+''+'975. Under Article 356 of the Constitution of India, President-s rule was imposed for the first time in. Answer: PEPSU  . Question'+
            ''+''+
            ''+''+'976. Patiala and East Punjab States Union (PEPSU) was a state of India between. Answer: 1948 and 1956.  . Question'+
            ''+''+
            ''+''+'977. The Political parties got the constitutional recognition for the first time in the year. Answer: 1985  . Question'+
            ''+''+
            ''+''+'978. When did Swami Vivekananda delivered his speech in "World Religion Conference" in Chicago city. Answer: 1893  . Question'+
            ''+''+
            ''+''+'979. Viticulture is. Answer: Production of grapes  . Question'+
            ''+''+
            ''+''+'980. The words "Satyameva jayate" inscribed below the base plate of the emblem of India are taken from. Answer: Mundaka Upanishad  . Question'+
            ''+''+
            ''+''+'981. The Khurda Road division,Odisha of the East Coast Railway (ECoR) has set a target to install bio-toilets in 2,000 train coaches during 2016-17 as part of the. Answer: Swachh Bharat Mission  . Question'+
            ''+''+
            ''+''+'982. Mrinalini Sarabhai is related with. Answer: Dance  . Question'+
            ''+''+
            ''+''+'983. Konark Temple was built by. Answer: king Narasimhadeva I  . Question'+
            ''+''+
            ''+''+'984. Smallest Continent of world. Answer: Australia  . Question'+
            ''+''+
            ''+''+'985. Marsh Gas. Answer: Methane  . Question'+
            ''+''+
            ''+''+'986. Who discovered penicillin. Answer: Alexander Fleming  . Question'+
            ''+''+
            ''+''+'987. Which of following chemicals is called as saltpeter. Answer: Potassium Nitrate  . Question'+
            ''+''+
            ''+''+'988. Which boxer is known as "Real Deal". Answer: Evander Holyfield  . Question'+
            ''+''+
            ''+''+'989. Which number of Lok Sabha was formed during 2014 election. Answer: 16th  . Question'+
            ''+''+
            ''+''+'990. Asif Ali hoisted flag in which movement. Answer: Quit India Movement  . Question'+
            ''+''+
            ''+''+'991. Who was commissioner of Delhi Police before Bassi. Answer: Neeraj Kumar  . Question'+
            ''+''+
            ''+''+'992. Who is Chairman of FIFA. Answer: Gianni Infantino  . Question'+
            ''+''+
            ''+''+'993. Abhishek Verma belongs to which sport. Answer: Archery  . Question'+
            ''+''+
            ''+''+'994. Which became first district with NOFN high speed connectivity. Answer: Idukki  . Question'+
            ''+''+
            ''+''+'995. Virupaksha temple is located at. Answer: Hampi  . Question'+
            ''+''+
            ''+''+'996. Which airport is working completely based on solar energy. Answer: Kochi Airport  . Question'+
            ''+''+
            ''+''+'997. State with Maximum boundaries with other states. Answer: Uttar Pradesh  . Question'+
            ''+''+
            ''+''+'998. Name to gandhi by British which he denied. Answer: Kaiser-e-Hind  . Question'+
            ''+''+
            ''+''+'999. Dada Saheb Phalke Award belongs to which field. Answer: Cinema  . Question'+
            ''+''+
            ''+''+'1000. 2015 Nobel Prize for literature winner. Answer: Bob Dylan')
        takeInput()
if __name__ == "__main__":
    takeInput()
