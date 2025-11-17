# Document: En Wikipedia Org Wiki Natural Language Processing

---

[Jump to content](#bodyContent)

Main menu

Main menu

move to sidebar hide

Navigation 

  * [Main page](/wiki/Main_Page "Visit the main page \[z\]")
  * [Contents](/wiki/Wikipedia:Contents "Guides to browsing Wikipedia")
  * [Current events](/wiki/Portal:Current_events "Articles related to current events")
  * [Random article](/wiki/Special:Random "Visit a randomly selected article \[x\]")
  * [About Wikipedia](/wiki/Wikipedia:About "Learn about Wikipedia and how it works")
  * [Contact us](//en.wikipedia.org/wiki/Wikipedia:Contact_us "How to contact Wikipedia")

Contribute 

  * [Help](/wiki/Help:Contents "Guidance on how to use and edit Wikipedia")
  * [Learn to edit](/wiki/Help:Introduction "Learn how to edit Wikipedia")
  * [Community portal](/wiki/Wikipedia:Community_portal "The hub for editors")
  * [Recent changes](/wiki/Special:RecentChanges "A list of recent changes to Wikipedia \[r\]")
  * [Upload file](/wiki/Wikipedia:File_upload_wizard "Add images or other media for use on Wikipedia")
  * [Special pages](/wiki/Special:SpecialPages)

[ ![](/static/images/icons/wikipedia.png) ![Wikipedia](/static/images/mobile/copyright/wikipedia-wordmark-en.svg) ![The Free Encyclopedia](/static/images/mobile/copyright/wikipedia-tagline-en.svg) ](/wiki/Main_Page)

[ Search ](/wiki/Special:Search "Search Wikipedia \[f\]")

Search

Appearance

  * [Donate](https://donate.wikimedia.org/?wmf_source=donate&wmf_medium=sidebar&wmf_campaign=en.wikipedia.org&uselang=en)
  * [Create account](/w/index.php?title=Special:CreateAccount&returnto=Natural+language+processing "You are encouraged to create an account and log in; however, it is not mandatory")
  * [Log in](/w/index.php?title=Special:UserLogin&returnto=Natural+language+processing "You're encouraged to log in; however, it's not mandatory. \[o\]")

Personal tools

  * [Donate](https://donate.wikimedia.org/?wmf_source=donate&wmf_medium=sidebar&wmf_campaign=en.wikipedia.org&uselang=en)
  * [ Create account](/w/index.php?title=Special:CreateAccount&returnto=Natural+language+processing "You are encouraged to create an account and log in; however, it is not mandatory")
  * [ Log in](/w/index.php?title=Special:UserLogin&returnto=Natural+language+processing "You're encouraged to log in; however, it's not mandatory. \[o\]")

## Contents

move to sidebar hide

  * [ (Top) ](#)
  * [ 1 History ](#History) Toggle History subsection
    * [ 1.1 Symbolic NLP (1950s – early 1990s) ](#Symbolic_NLP_\(1950s_–_early_1990s\))
    * [ 1.2 Statistical NLP (1990s–present) ](#Statistical_NLP_\(1990s–present\))
  * [ 2 Approaches: Symbolic, statistical, neural networks ](#Approaches:_Symbolic,_statistical,_neural_networks) Toggle Approaches: Symbolic, statistical, neural networks subsection
    * [ 2.1 Statistical approach ](#Statistical_approach)
    * [ 2.2 Neural networks ](#Neural_networks)
  * [ 3 Common NLP tasks ](#Common_NLP_tasks) Toggle Common NLP tasks subsection
    * [ 3.1 Text and speech processing ](#Text_and_speech_processing)
    * [ 3.2 Morphological analysis ](#Morphological_analysis)
    * [ 3.3 Syntactic analysis ](#Syntactic_analysis)
    * [ 3.4 Lexical semantics (of individual words in context) ](#Lexical_semantics_\(of_individual_words_in_context\))
    * [ 3.5 Relational semantics (semantics of individual sentences) ](#Relational_semantics_\(semantics_of_individual_sentences\))
    * [ 3.6 Discourse (semantics beyond individual sentences) ](#Discourse_\(semantics_beyond_individual_sentences\))
    * [ 3.7 Higher-level NLP applications ](#Higher-level_NLP_applications)
  * [ 4 General tendencies and (possible) future directions ](#General_tendencies_and_\(possible\)_future_directions) Toggle General tendencies and (possible) future directions subsection
    * [ 4.1 Cognition ](#Cognition)
  * [ 5 See also ](#See_also)
  * [ 6 References ](#References)
  * [ 7 Further reading ](#Further_reading)
  * [ 8 External links ](#External_links)

Toggle the table of contents

# Natural language processing

71 languages

  * [Afrikaans](https://af.wikipedia.org/wiki/Natuurliketaalverwerking "Natuurliketaalverwerking – Afrikaans")
  * [العربية](https://ar.wikipedia.org/wiki/%D9%85%D8%B9%D8%A7%D9%84%D8%AC%D8%A9_%D8%A7%D9%84%D9%84%D8%BA%D8%A9_%D8%A7%D9%84%D8%B7%D8%A8%D9%8A%D8%B9%D9%8A%D8%A9 "معالجة اللغة الطبيعية – Arabic")
  * [Արեւմտահայերէն](https://hyw.wikipedia.org/wiki/%D4%B2%D5%B6%D5%A1%D5%AF%D5%A1%D5%B6_%D4%BC%D5%A5%D5%A6%D5%B8%D6%82%D5%AB_%D5%84%D5%B7%D5%A1%D5%AF%D5%B8%D6%82%D5%B4 "Բնական Լեզուի Մշակում – Western Armenian")
  * [Azərbaycanca](https://az.wikipedia.org/wiki/T%C9%99bii_dilin_emal%C4%B1 "Təbii dilin emalı – Azerbaijani")
  * [বাংলা](https://bn.wikipedia.org/wiki/%E0%A6%B8%E0%A7%8D%E0%A6%AC%E0%A6%BE%E0%A6%AD%E0%A6%BE%E0%A6%AC%E0%A6%BF%E0%A6%95_%E0%A6%AD%E0%A6%BE%E0%A6%B7%E0%A6%BE_%E0%A6%AA%E0%A7%8D%E0%A6%B0%E0%A6%95%E0%A7%8D%E0%A6%B0%E0%A6%BF%E0%A6%AF%E0%A6%BC%E0%A6%BE%E0%A6%9C%E0%A6%BE%E0%A6%A4%E0%A6%95%E0%A6%B0%E0%A6%A3 "স্বাভাবিক ভাষা প্রক্রিয়াজাতকরণ – Bangla")
  * [閩南語 / Bân-lâm-gí](https://zh-min-nan.wikipedia.org/wiki/Ch%C5%AB-ji%C3%A2n_gi%C3%A2n-g%C3%BA_chh%C3%BA-l%C3%AD "Chū-jiân giân-gú chhú-lí – Minnan")
  * [Беларуская](https://be.wikipedia.org/wiki/%D0%90%D0%BF%D1%80%D0%B0%D1%86%D0%BE%D1%9E%D0%BA%D0%B0_%D0%BD%D0%B0%D1%82%D1%83%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D0%B9_%D0%BC%D0%BE%D0%B2%D1%8B "Апрацоўка натуральнай мовы – Belarusian")
  * [Беларуская (тарашкевіца)](https://be-tarask.wikipedia.org/wiki/%D0%90%D0%BF%D1%80%D0%B0%D1%86%D0%BE%D1%9E%D0%BA%D0%B0_%D0%BD%D0%B0%D1%82%D1%83%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D0%B9_%D0%BC%D0%BE%D0%B2%D1%8B "Апрацоўка натуральнай мовы – Belarusian \(Taraškievica orthography\)")
  * [Български](https://bg.wikipedia.org/wiki/%D0%9E%D0%B1%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B0_%D0%BD%D0%B0_%D0%B5%D1%81%D1%82%D0%B5%D1%81%D1%82%D0%B2%D0%B5%D0%BD_%D0%B5%D0%B7%D0%B8%D0%BA "Обработка на естествен език – Bulgarian")
  * [Bosanski](https://bs.wikipedia.org/wiki/Obrada_prirodnog_jezika "Obrada prirodnog jezika – Bosnian")
  * [Brezhoneg](https://br.wikipedia.org/wiki/Treterezh_emgefre_al_lavar "Treterezh emgefre al lavar – Breton")
  * [Català](https://ca.wikipedia.org/wiki/Processament_del_llenguatge_natural "Processament del llenguatge natural – Catalan")
  * [Čeština](https://cs.wikipedia.org/wiki/Zpracov%C3%A1n%C3%AD_p%C5%99irozen%C3%A9ho_jazyka "Zpracování přirozeného jazyka – Czech")
  * [Cymraeg](https://cy.wikipedia.org/wiki/Prosesu_Iaith_Naturiol "Prosesu Iaith Naturiol – Welsh")
  * [Dansk](https://da.wikipedia.org/wiki/Sprogteknologi "Sprogteknologi – Danish")
  * [Deutsch](https://de.wikipedia.org/wiki/Verarbeitung_nat%C3%BCrlicher_Sprache "Verarbeitung natürlicher Sprache – German")
  * [Eesti](https://et.wikipedia.org/wiki/Loomuliku_keele_t%C3%B6%C3%B6tlus "Loomuliku keele töötlus – Estonian")
  * [Ελληνικά](https://el.wikipedia.org/wiki/%CE%95%CF%80%CE%B5%CE%BE%CE%B5%CF%81%CE%B3%CE%B1%CF%83%CE%AF%CE%B1_%CF%86%CF%85%CF%83%CE%B9%CE%BA%CE%AE%CF%82_%CE%B3%CE%BB%CF%8E%CF%83%CF%83%CE%B1%CF%82 "Επεξεργασία φυσικής γλώσσας – Greek")
  * [Español](https://es.wikipedia.org/wiki/Procesamiento_de_lenguajes_naturales "Procesamiento de lenguajes naturales – Spanish")
  * [Esperanto](https://eo.wikipedia.org/wiki/Natur-lingva_prilaborado "Natur-lingva prilaborado – Esperanto")
  * [Euskara](https://eu.wikipedia.org/wiki/Hizkuntzaren_prozesamendu "Hizkuntzaren prozesamendu – Basque")
  * [فارسی](https://fa.wikipedia.org/wiki/%D9%BE%D8%B1%D8%AF%D8%A7%D8%B2%D8%B4_%D8%B2%D8%A8%D8%A7%D9%86%E2%80%8C%D9%87%D8%A7%DB%8C_%D8%B7%D8%A8%DB%8C%D8%B9%DB%8C "پردازش زبان‌های طبیعی – Persian")
  * [Français](https://fr.wikipedia.org/wiki/Traitement_automatique_des_langues "Traitement automatique des langues – French")
  * [Gaeilge](https://ga.wikipedia.org/wiki/Pr%C3%B3ise%C3%A1il_teanga_n%C3%A1d%C3%BArtha "Próiseáil teanga nádúrtha – Irish")
  * [Galego](https://gl.wikipedia.org/wiki/Procesamento_da_linguaxe_natural "Procesamento da linguaxe natural – Galician")
  * [한국어](https://ko.wikipedia.org/wiki/%EC%9E%90%EC%97%B0%EC%96%B4_%EC%B2%98%EB%A6%AC "자연어 처리 – Korean")
  * [Հայերեն](https://hy.wikipedia.org/wiki/%D4%B2%D5%B6%D5%A1%D5%AF%D5%A1%D5%B6_%D5%AC%D5%A5%D5%A6%D5%BE%D5%AB_%D5%B4%D5%B7%D5%A1%D5%AF%D5%B8%D6%82%D5%B4 "Բնական լեզվի մշակում – Armenian")
  * [हिन्दी](https://hi.wikipedia.org/wiki/%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A4%BE%E0%A4%95%E0%A5%83%E0%A4%A4%E0%A4%BF%E0%A4%95_%E0%A4%AD%E0%A4%BE%E0%A4%B7%E0%A4%BE_%E0%A4%B8%E0%A4%82%E0%A4%B8%E0%A4%BE%E0%A4%A7%E0%A4%A8 "प्राकृतिक भाषा संसाधन – Hindi")
  * [Hrvatski](https://hr.wikipedia.org/wiki/Obrada_prirodnog_jezika "Obrada prirodnog jezika – Croatian")
  * [Ido](https://io.wikipedia.org/wiki/Procedo_pri_naturala_linguo "Procedo pri naturala linguo – Ido")
  * [Bahasa Indonesia](https://id.wikipedia.org/wiki/Pengolahan_bahasa_alami "Pengolahan bahasa alami – Indonesian")
  * [IsiZulu](https://zu.wikipedia.org/wiki/Ukudludlunga_ulimi_lwemvelo "Ukudludlunga ulimi lwemvelo – Zulu")
  * [Íslenska](https://is.wikipedia.org/wiki/M%C3%A1lgreining "Málgreining – Icelandic")
  * [Italiano](https://it.wikipedia.org/wiki/Elaborazione_del_linguaggio_naturale "Elaborazione del linguaggio naturale – Italian")
  * [עברית](https://he.wikipedia.org/wiki/%D7%A2%D7%99%D7%91%D7%95%D7%93_%D7%A9%D7%A4%D7%94_%D7%98%D7%91%D7%A2%D7%99%D7%AA "עיבוד שפה טבעית – Hebrew")
  * [ಕನ್ನಡ](https://kn.wikipedia.org/wiki/%E0%B2%B8%E0%B2%B9%E0%B2%9C_%E0%B2%AD%E0%B2%BE%E0%B2%B7%E0%B2%BE_%E0%B2%B8%E0%B2%82%E0%B2%B8%E0%B3%8D%E0%B2%95%E0%B2%B0%E0%B2%A3%E0%B3%86 "ಸಹಜ ಭಾಷಾ ಸಂಸ್ಕರಣೆ – Kannada")
  * [ქართული](https://ka.wikipedia.org/wiki/%E1%83%91%E1%83%A3%E1%83%9C%E1%83%94%E1%83%91%E1%83%A0%E1%83%98%E1%83%95%E1%83%98_%E1%83%94%E1%83%9C%E1%83%98%E1%83%A1_%E1%83%93%E1%83%90%E1%83%9B%E1%83%A3%E1%83%A8%E1%83%90%E1%83%95%E1%83%94%E1%83%91%E1%83%90 "ბუნებრივი ენის დამუშავება – Georgian")
  * [Latviešu](https://lv.wikipedia.org/wiki/Dabisk%C4%81s_valodas_apstr%C4%81de "Dabiskās valodas apstrāde – Latvian")
  * [Lietuvių](https://lt.wikipedia.org/wiki/Nat%C5%ABraliosios_kalbos_apdorojimas "Natūraliosios kalbos apdorojimas – Lithuanian")
  * [Македонски](https://mk.wikipedia.org/wiki/%D0%9E%D0%B1%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B0_%D0%BD%D0%B0_%D0%BF%D1%80%D0%B8%D1%80%D0%BE%D0%B4%D0%BD%D0%B8_%D1%98%D0%B0%D0%B7%D0%B8%D1%86%D0%B8 "Обработка на природни јазици – Macedonian")
  * [मराठी](https://mr.wikipedia.org/wiki/%E0%A4%A8%E0%A5%88%E0%A4%B8%E0%A4%B0%E0%A5%8D%E0%A4%97%E0%A4%BF%E0%A4%95_%E0%A4%AD%E0%A4%BE%E0%A4%B7%E0%A4%BE_%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A4%95%E0%A5%8D%E0%A4%B0%E0%A4%BF%E0%A4%AF%E0%A4%BE "नैसर्गिक भाषा प्रक्रिया – Marathi")
  * [مصرى](https://arz.wikipedia.org/wiki/%D8%AA%D8%AD%D9%84%D9%8A%D9%84_%D8%A7%D9%84%D9%84%D8%BA%D8%A7%D8%AA_%D8%A7%D9%84%D8%B7%D8%A8%D9%8A%D8%B9%D9%8A%D9%87 "تحليل اللغات الطبيعيه – Egyptian Arabic")
  * [Монгол](https://mn.wikipedia.org/wiki/%D0%9A%D0%BE%D0%BC%D0%BF%D1%8C%D1%8E%D1%82%D0%B5%D1%80%D1%8B%D0%BD_%D1%85%D1%8D%D0%BB_%D1%88%D0%B8%D0%BD%D0%B6%D0%BB%D1%8D%D0%BB "Компьютерын хэл шинжлэл – Mongolian")
  * [မြန်မာဘာသာ](https://my.wikipedia.org/wiki/%E1%80%99%E1%80%AD%E1%80%81%E1%80%84%E1%80%BA%E1%80%98%E1%80%AC%E1%80%9E%E1%80%AC%E1%80%85%E1%80%80%E1%80%AC%E1%80%B8%E1%80%9E%E1%80%AF%E1%80%B6%E1%80%B8_%E1%80%80%E1%80%BD%E1%80%94%E1%80%BA%E1%80%95%E1%80%BB%E1%80%B0%E1%80%90%E1%80%AC%E1%80%85%E1%80%94%E1%80%85%E1%80%BA "မိခင်ဘာသာစကားသုံး ကွန်ပျူတာစနစ် – Burmese")
  * [Nederlands](https://nl.wikipedia.org/wiki/Taaltechnologie "Taaltechnologie – Dutch")
  * [日本語](https://ja.wikipedia.org/wiki/%E8%87%AA%E7%84%B6%E8%A8%80%E8%AA%9E%E5%87%A6%E7%90%86 "自然言語処理 – Japanese")
  * [Norsk bokmål](https://no.wikipedia.org/wiki/Spr%C3%A5kteknologi "Språkteknologi – Norwegian Bokmål")
  * [ଓଡ଼ିଆ](https://or.wikipedia.org/wiki/%E0%AC%A8%E0%AD%8D%E0%AD%9F%E0%AC%BE%E0%AC%9A%E0%AD%81%E0%AC%B0%E0%AC%BE%E0%AC%B2_%E0%AC%B2%E0%AC%BE%E0%AC%99%E0%AD%8D%E0%AC%97%E0%AD%81%E0%AC%8F%E0%AC%9C_%E0%AC%AA%E0%AD%8D%E0%AC%B0%E0%AD%8B%E0%AC%B8%E0%AD%87%E0%AC%B8%E0%AC%BF%E0%AC%82 "ନ୍ୟାଚୁରାଲ ଲାଙ୍ଗୁଏଜ ପ୍ରୋସେସିଂ – Odia")
  * [پښتو](https://ps.wikipedia.org/wiki/%D8%AF_%D8%B7%D8%A8%D9%8A%D8%B9%D9%8A_%DA%98%D8%A8%DB%90_%D9%BE%D8%B1%D9%88%D8%B3%D8%B3_%DA%A9%D9%88%D9%84 "د طبيعي ژبې پروسس کول – Pashto")
  * [Picard](https://pcd.wikipedia.org/wiki/Traitemint_automatique_d%27ches_langues "Traitemint automatique d'ches langues – Picard")
  * [Piemontèis](https://pms.wikipedia.org/wiki/NLP "NLP – Piedmontese")
  * [Polski](https://pl.wikipedia.org/wiki/Przetwarzanie_j%C4%99zyka_naturalnego "Przetwarzanie języka naturalnego – Polish")
  * [Português](https://pt.wikipedia.org/wiki/Processamento_de_linguagem_natural "Processamento de linguagem natural – Portuguese")
  * [Qaraqalpaqsha](https://kaa.wikipedia.org/wiki/T%C3%A1biyiy_tildi_qayta_islew "Tábiyiy tildi qayta islew – Kara-Kalpak")
  * [Română](https://ro.wikipedia.org/wiki/Prelucrarea_limbajului_natural "Prelucrarea limbajului natural – Romanian")
  * [Runa Simi](https://qu.wikipedia.org/wiki/Purum_simi_thatkichay "Purum simi thatkichay – Quechua")
  * [Русский](https://ru.wikipedia.org/wiki/%D0%9E%D0%B1%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B0_%D0%B5%D1%81%D1%82%D0%B5%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D0%BE%D0%B3%D0%BE_%D1%8F%D0%B7%D1%8B%D0%BA%D0%B0 "Обработка естественного языка – Russian")
  * [Shqip](https://sq.wikipedia.org/wiki/P%C3%ABrpunimi_i_gjuh%C3%ABs_natyrore "Përpunimi i gjuhës natyrore – Albanian")
  * [Simple English](https://simple.wikipedia.org/wiki/Natural_language_processing "Natural language processing – Simple English")
  * [کوردی](https://ckb.wikipedia.org/wiki/%D9%BE%DB%8E%D9%88%D8%A7%DA%98%DB%86%DA%A9%D8%B1%D8%AF%D9%86%DB%8C_%D8%B2%D9%85%D8%A7%D9%86%DB%8C_%D8%B3%D8%B1%D9%88%D8%B4%D8%AA%DB%8C "پێواژۆکردنی زمانی سروشتی – Central Kurdish")
  * [Српски / srpski](https://sr.wikipedia.org/wiki/Obrada_prirodnih_jezika "Obrada prirodnih jezika – Serbian")
  * [Srpskohrvatski / српскохрватски](https://sh.wikipedia.org/wiki/Obrada_prirodnih_jezika "Obrada prirodnih jezika – Serbo-Croatian")
  * [Suomi](https://fi.wikipedia.org/wiki/Luonnollisen_kielen_k%C3%A4sittely "Luonnollisen kielen käsittely – Finnish")
  * [தமிழ்](https://ta.wikipedia.org/wiki/%E0%AE%87%E0%AE%AF%E0%AE%B1%E0%AF%8D%E0%AE%95%E0%AF%88_%E0%AE%AE%E0%AF%8A%E0%AE%B4%E0%AE%BF_%E0%AE%AE%E0%AF%81%E0%AE%B1%E0%AF%88%E0%AE%AF%E0%AE%BE%E0%AE%95%E0%AF%8D%E0%AE%95%E0%AE%AE%E0%AF%8D "இயற்கை மொழி முறையாக்கம் – Tamil")
  * [తెలుగు](https://te.wikipedia.org/wiki/%E0%B0%B8%E0%B0%B9%E0%B0%9C_%E0%B0%AD%E0%B0%BE%E0%B0%B7%E0%B0%BE_%E0%B0%AA%E0%B1%8D%E0%B0%B0%E0%B0%95%E0%B1%8D%E0%B0%B0%E0%B0%BF%E0%B0%AF "సహజ భాషా ప్రక్రియ – Telugu")
  * [ไทย](https://th.wikipedia.org/wiki/%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%9B%E0%B8%A3%E0%B8%B0%E0%B8%A1%E0%B8%A7%E0%B8%A5%E0%B8%A0%E0%B8%B2%E0%B8%A9%E0%B8%B2%E0%B8%98%E0%B8%A3%E0%B8%A3%E0%B8%A1%E0%B8%8A%E0%B8%B2%E0%B8%95%E0%B8%B4 "การประมวลภาษาธรรมชาติ – Thai")
  * [Türkçe](https://tr.wikipedia.org/wiki/Do%C4%9Fal_dil_i%C5%9Fleme "Doğal dil işleme – Turkish")
  * [Українська](https://uk.wikipedia.org/wiki/%D0%9E%D0%B1%D1%80%D0%BE%D0%B1%D0%BA%D0%B0_%D0%BF%D1%80%D0%B8%D1%80%D0%BE%D0%B4%D0%BD%D0%BE%D1%97_%D0%BC%D0%BE%D0%B2%D0%B8 "Обробка природної мови – Ukrainian")
  * [Tiếng Việt](https://vi.wikipedia.org/wiki/X%E1%BB%AD_l%C3%BD_ng%C3%B4n_ng%E1%BB%AF_t%E1%BB%B1_nhi%C3%AAn "Xử lý ngôn ngữ tự nhiên – Vietnamese")
  * [粵語](https://zh-yue.wikipedia.org/wiki/%E8%87%AA%E7%84%B6%E8%AA%9E%E8%A8%80%E8%99%95%E7%90%86 "自然語言處理 – Cantonese")
  * [中文](https://zh.wikipedia.org/wiki/%E8%87%AA%E7%84%B6%E8%AF%AD%E8%A8%80%E5%A4%84%E7%90%86 "自然语言处理 – Chinese")

[Edit links](https://www.wikidata.org/wiki/Special:EntityPage/Q30642#sitelinks-wikipedia "Edit interlanguage links")

  * [Article](/wiki/Natural_language_processing "View the content page \[c\]")
  * [Talk](/wiki/Talk:Natural_language_processing "Discuss improvements to the content page \[t\]")

English

  * [Read](/wiki/Natural_language_processing)
  * [Edit](/w/index.php?title=Natural_language_processing&action=edit "Edit this page \[e\]")
  * [View history](/w/index.php?title=Natural_language_processing&action=history "Past revisions of this page \[h\]")

Tools

Tools

move to sidebar hide

Actions 

  * [Read](/wiki/Natural_language_processing)
  * [Edit](/w/index.php?title=Natural_language_processing&action=edit "Edit this page \[e\]")
  * [View history](/w/index.php?title=Natural_language_processing&action=history)

General 

  * [What links here](/wiki/Special:WhatLinksHere/Natural_language_processing "List of all English Wikipedia pages containing links to this page \[j\]")
  * [Related changes](/wiki/Special:RecentChangesLinked/Natural_language_processing "Recent changes in pages linked from this page \[k\]")
  * [Upload file](//en.wikipedia.org/wiki/Wikipedia:File_Upload_Wizard "Upload files \[u\]")
  * [Permanent link](/w/index.php?title=Natural_language_processing&oldid=1321938724 "Permanent link to this revision of this page")
  * [Page information](/w/index.php?title=Natural_language_processing&action=info "More information about this page")
  * [Cite this page](/w/index.php?title=Special:CiteThisPage&page=Natural_language_processing&id=1321938724&wpFormIdentifier=titleform "Information on how to cite this page")
  * [Get shortened URL](/w/index.php?title=Special:UrlShortener&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FNatural_language_processing)
  * [Download QR code](/w/index.php?title=Special:QrCode&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FNatural_language_processing)

Print/export 

  * [Download as PDF](/w/index.php?title=Special:DownloadAsPdf&page=Natural_language_processing&action=show-download-screen "Download this page as a PDF file")
  * [Printable version](/w/index.php?title=Natural_language_processing&printable=yes "Printable version of this page \[p\]")

In other projects 

  * [Wikimedia Commons](https://commons.wikimedia.org/wiki/Category:Natural_language_processing)
  * [Wikiversity](https://en.wikiversity.org/wiki/Natural_Language_Processing)
  * [Wikidata item](https://www.wikidata.org/wiki/Special:EntityPage/Q30642 "Structured data on this page hosted by Wikidata \[g\]")

Appearance

move to sidebar hide

From Wikipedia, the free encyclopedia

Processing of natural language by a computer

![](//upload.wikimedia.org/wikipedia/en/thumb/b/b4/Ambox_important.svg/40px-Ambox_important.svg.png)| **This article has multiple issues.** Please help **[improve it](/wiki/Special:EditPage/Natural_language_processing "Special:EditPage/Natural language processing")** or discuss these issues on the **[talk page](/wiki/Talk:Natural_language_processing "Talk:Natural language processing")**. _([Learn how and when to remove these messages](/wiki/Help:Maintenance_template_removal "Help:Maintenance template removal"))_ | [![](//upload.wikimedia.org/wikipedia/en/thumb/9/99/Question_book-new.svg/60px-Question_book-new.svg.png)](/wiki/File:Question_book-new.svg)| This article **needs additional citations for[verification](/wiki/Wikipedia:Verifiability "Wikipedia:Verifiability")**. Please help [improve this article](/wiki/Special:EditPage/Natural_language_processing "Special:EditPage/Natural language processing") by [adding citations to reliable sources](/wiki/Help:Referencing_for_beginners "Help:Referencing for beginners"). Unsourced material may be challenged and removed.  
_Find sources:_ ["Natural language processing"](https://www.google.com/search?as_eq=wikipedia&q=%22Natural+language+processing%22) – [news](https://www.google.com/search?tbm=nws&q=%22Natural+language+processing%22+-wikipedia&tbs=ar:1) **·** [newspapers](https://www.google.com/search?&q=%22Natural+language+processing%22&tbs=bkt:s&tbm=bks) **·** [books](https://www.google.com/search?tbs=bks:1&q=%22Natural+language+processing%22+-wikipedia) **·** [scholar](https://scholar.google.com/scholar?q=%22Natural+language+processing%22) **·** [JSTOR](https://www.jstor.org/action/doBasicSearch?Query=%22Natural+language+processing%22&acc=on&wc=on) _( May 2024)__([Learn how and when to remove this message](/wiki/Help:Maintenance_template_removal "Help:Maintenance template removal"))_  
---|---  
[![](//upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Crystal_Clear_app_kedit.svg/40px-Crystal_Clear_app_kedit.svg.png)](/wiki/File:Crystal_Clear_app_kedit.svg)| This article **may need to be rewritten** to comply with Wikipedia's [quality standards](/wiki/Wikipedia:Manual_of_Style "Wikipedia:Manual of Style"). [You can help](https://en.wikipedia.org/w/index.php?title=Natural_language_processing&action=edit). The [talk page](/wiki/Talk:Natural_language_processing "Talk:Natural language processing") may contain suggestions. _( July 2025)_  
---|---  
![](//upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Ambox_rewrite.svg/40px-Ambox_rewrite.svg.png)| This article **may be in need of reorganization to comply with Wikipedia's[layout guidelines](/wiki/Wikipedia:Manual_of_Style/Layout "Wikipedia:Manual of Style/Layout")**. Please help by [editing the article](https://en.wikipedia.org/w/index.php?title=Natural_language_processing&action=edit) to make improvements to the overall structure. _( July 2025)__([Learn how and when to remove this message](/wiki/Help:Maintenance_template_removal "Help:Maintenance template removal"))_  
---|---  
  
_([Learn how and when to remove this message](/wiki/Help:Maintenance_template_removal "Help:Maintenance template removal"))_  
  
**Natural language processing** (**NLP**) is the processing of [natural language](/wiki/Natural_language "Natural language") information by a [computer](/wiki/Computer "Computer"). The study of NLP, a subfield of [computer science](/wiki/Computer_science "Computer science"), is generally associated with [artificial intelligence](/wiki/Artificial_intelligence "Artificial intelligence"). NLP is related to [information retrieval](/wiki/Information_retrieval "Information retrieval"), [knowledge representation](/wiki/Knowledge_representation "Knowledge representation"), [computational linguistics](/wiki/Computational_linguistics "Computational linguistics"), and more broadly with [linguistics](/wiki/Linguistics "Linguistics").[[1]](#cite_note-nlpintro-1)

Major processing tasks in an NLP system include: [speech recognition](/wiki/Speech_recognition "Speech recognition"), [text classification](/wiki/Text_classification "Text classification"), [natural language understanding](/wiki/Natural-language_understanding "Natural-language understanding"), and [natural language generation](/wiki/Natural_language_generation "Natural language generation"). 

## History

[[edit](/w/index.php?title=Natural_language_processing&action=edit&section=1 "Edit section: History")]

Further information: [History of natural language processing](/wiki/History_of_natural_language_processing "History of natural language processing")

Natural language processing has its roots in the 1950s.[[2]](#cite_note-2) Already in 1950, [Alan Turing](/wiki/Alan_Turing "Alan Turing") published an article titled "[Computing Machinery and Intelligence](/wiki/Computing_Machinery_and_Intelligence "Computing Machinery and Intelligence")" which proposed what is now called the [Turing test](/wiki/Turing_test "Turing test") as a criterion of intelligence, though at the time that was not articulated as a problem separate from artificial intelligence. The proposed test includes a task that involves the automated interpretation and generation of natural language. 

### Symbolic NLP (1950s – early 1990s)

[[edit](/w/index.php?title=Natural_language_processing&action=edit&section=2 "Edit section: Symbolic NLP \(1950s – early 1990s\)")]

[![](//upload.wikimedia.org/wikipedia/commons/thumb/0/09/AST_Document.svg/250px-AST_Document.svg.png)](/wiki/File:AST_Document.svg)A document parsed into an abstract syntax tree

The premise of symbolic NLP is well-summarized by [John Searle](/wiki/John_Searle "John Searle")'s [Chinese room](/wiki/Chinese_room "Chinese room") experiment: Given a collection of rules (e.g., a Chinese phrasebook, with questions and matching answers), the computer emulates natural language understanding (or other NLP tasks) by applying those rules to the data it confronts. 

  * **1950s** : The [Georgetown experiment](/wiki/Georgetown-IBM_experiment "Georgetown-IBM experiment") in 1954 involved fully [automatic translation](/wiki/Automatic_translation "Automatic translation") of more than sixty Russian sentences into English. The authors claimed that within three or five years, machine translation would be a solved problem.[[3]](#cite_note-3) However, real progress was much slower, and after the [ALPAC report](/wiki/ALPAC "ALPAC") in 1966, which found that ten years of research had failed to fulfill the expectations, funding for machine translation was dramatically reduced. Little further research in machine translation was conducted in America (though some research continued elsewhere, such as Japan and Europe[[4]](#cite_note-4)) until the late 1980s when the first [statistical machine translation](/wiki/Statistical_machine_translation "Statistical machine translation") systems were developed.
  * **1960s** : Some notably successful natural language processing systems developed in the 1960s were [SHRDLU](/wiki/SHRDLU "SHRDLU"), a natural language system working in restricted "[blocks worlds](/wiki/Blocks_world "Blocks world")" with restricted vocabularies, and [ELIZA](/wiki/ELIZA "ELIZA"), a simulation of a [Rogerian psychotherapist](/wiki/Rogerian_psychotherapy "Rogerian psychotherapy"), written by [Joseph Weizenbaum](/wiki/Joseph_Weizenbaum "Joseph Weizenbaum") between 1964 and 1966. Using almost no information about human thought or emotion, ELIZA sometimes provided a startlingly human-like interaction. When the "patient" exceeded the very small knowledge base, ELIZA might provide a generic response, for example, responding to "My head hurts" with "Why do you say your head hurts?". Ross Quillian's successful work on natural language was demonstrated with a vocabulary of only _twenty_ words, because that was all that would fit in a computer memory at the time.[[5]](#cite_note-5)

  * **1970s** : During the 1970s, many programmers began to write "conceptual [ontologies](/wiki/Ontology_\(information_science\) "Ontology \(information science\)")", which structured real-world information into computer-understandable data. Examples are MARGIE (Schank, 1975), SAM (Cullingford, 1978), PAM (Wilensky, 1978), TaleSpin (Meehan, 1976), QUALM (Lehnert, 1977), Politics (Carbonell, 1979), and Plot Units (Lehnert 1981). During this time, the first [chatterbots](/wiki/Chatterbots "Chatterbots") were written (e.g., [PARRY](/wiki/PARRY "PARRY")).
  * **1980s** : The 1980s and early 1990s mark the heyday of symbolic methods in NLP. Focus areas of the time included research on rule-based parsing (e.g., the development of [HPSG](/wiki/Head-driven_phrase_structure_grammar "Head-driven phrase structure grammar") as a computational operationalization of [generative grammar](/wiki/Generative_grammar "Generative grammar")), morphology (e.g., two-level morphology[[6]](#cite_note-6)), semantics (e.g., [Lesk algorithm](/wiki/Lesk_algorithm "Lesk algorithm")), reference (e.g., within Centering Theory[[7]](#cite_note-7)) and other areas of natural language understanding (e.g., in the [Rhetorical Structure Theory](/wiki/Rhetorical_structure_theory "Rhetorical structure theory")). Other lines of research were continued, e.g., the development of chatterbots with [Racter](/wiki/Racter "Racter") and [Jabberwacky](/wiki/Jabberwacky "Jabberwacky"). An important development (that eventually led to the statistical turn in the 1990s) was the rising importance of quantitative evaluation in this period.[[8]](#cite_note-8)

### Statistical NLP (1990s–present)

[[edit](/w/index.php?title=Natural_language_processing&action=edit&section=3 "Edit section: Statistical NLP \(1990s–present\)")]

Up until the 1980s, most natural language processing systems were based on complex sets of hand-written rules. Starting in the late 1980s, however, there was a revolution in natural language processing with the introduction of [machine learning](/wiki/Machine_learning "Machine learning") algorithms for language processing. This was due to both the steady increase in computational power (see [Moore's law](/wiki/Moore%27s_law "Moore's law")) and the gradual lessening of the dominance of [Chomskyan](/wiki/Noam_Chomsky "Noam Chomsky") theories of linguistics (e.g. [transformational grammar](/wiki/Transformational_grammar "Transformational grammar")), whose theoretical underpinnings discouraged the sort of [corpus linguistics](/wiki/Corpus_linguistics "Corpus linguistics") that underlies the machine-learning approach to language processing.[[9]](#cite_note-9)

  * **1990s** : Many of the notable early successes in statistical methods in NLP occurred in the field of [machine translation](/wiki/Machine_translation "Machine translation"), due especially to work at IBM Research, such as [IBM alignment models](/wiki/IBM_alignment_models "IBM alignment models"). These systems were able to take advantage of existing multilingual [textual corpora](/wiki/Text_corpus "Text corpus") that had been produced by the [Parliament of Canada](/wiki/Parliament_of_Canada "Parliament of Canada") and the [European Union](/wiki/European_Union "European Union") as a result of laws calling for the translation of all governmental proceedings into all official languages of the corresponding systems of government. However, most other systems depended on corpora specifically developed for the tasks implemented by these systems, which was (and often continues to be) a major limitation in the success of these systems. As a result, a great deal of research has gone into methods of more effectively learning from limited amounts of data.
  * **2000s** : With the growth of the web, increasing amounts of raw (unannotated) language data have become available since the mid-1990s. Research has thus increasingly focused on [unsupervised](/wiki/Unsupervised_learning "Unsupervised learning") and [semi-supervised learning](/wiki/Semi-supervised_learning "Semi-supervised learning") algorithms. Such algorithms can learn from data that has not been hand-annotated with the desired answers or using a combination of annotated and non-annotated data. Generally, this task is much more difficult than [supervised learning](/wiki/Supervised_learning "Supervised learning"), and typically produces less accurate results for a given amount of input data. However, there is an enormous amount of non-annotated data available (including, among other things, the entire content of the [World Wide Web](/wiki/World_Wide_Web "World Wide Web")), which can often make up for the worse efficiency if the algorithm used has a low enough [time complexity](/wiki/Time_complexity "Time complexity") to be practical.
  * **2003:** [word n-gram model](/wiki/Word_n-gram_language_model "Word n-gram language model"), at the time the best statistical algorithm, is outperformed by a [multi-layer perceptron](/wiki/Multi-layer_perceptron "Multi-layer perceptron") (with a single hidden layer and context length of several words, trained on up to 14 million words, by [Bengio](/wiki/Yoshua_Bengio "Yoshua Bengio") et al.)[[10]](#cite_note-10)
  * **2010:** [Tomáš Mikolov](/wiki/Tom%C3%A1%C5%A1_Mikolov "Tomáš Mikolov") (then a PhD student at [Brno University of Technology](/wiki/Brno_University_of_Technology "Brno University of Technology")) with co-authors applied a simple [recurrent neural network](/wiki/Recurrent_neural_network "Recurrent neural network") with a single hidden layer to language modelling,[[11]](#cite_note-11) and in the following years he went on to develop [Word2vec](/wiki/Word2vec "Word2vec"). In the 2010s, [representation learning](/wiki/Representation_learning "Representation learning") and [deep neural network](/wiki/Deep_learning "Deep learning")-style (featuring many hidden layers) machine learning methods became widespread in natural language processing. That popularity was due partly to a flurry of results showing that such techniques[[12]](#cite_note-goldberg:nnlp17-12)[[13]](#cite_note-goodfellow:book16-13) can achieve state-of-the-art results in many natural language tasks, e.g., in [language modeling](/wiki/Language_modeling "Language modeling")[[14]](#cite_note-jozefowicz:lm16-14) and parsing.[[15]](#cite_note-choe:emnlp16-15)[[16]](#cite_note-vinyals:nips15-16) This is increasingly important [in medicine and healthcare](/wiki/Artificial_intelligence_in_healthcare "Artificial intelligence in healthcare"), where NLP helps analyze notes and text in [electronic health records](/wiki/Electronic_health_record "Electronic health record") that would otherwise be inaccessible for study when seeking to improve care[[17]](#cite_note-17) or protect patient privacy.[[18]](#cite_note-18)

## Approaches: Symbolic, statistical, neural networks

[[edit](/w/index.php?title=Natural_language_processing&action=edit&section=4 "Edit section: Approaches: Symbolic, statistical, neural networks")]

Symbolic approach, i.e., the hand-coding of a set of rules for manipulating symbols, coupled with a dictionary lookup, was historically the first approach used both by AI in general and by NLP in particular:[[19]](#cite_note-winograd:shrdlu71-19)[[20]](#cite_note-schank77-20) such as by writing grammars or devising heuristic rules for [stemming](/wiki/Stemming "Stemming"). 

[Machine learning](/wiki/Machine_learning "Machine learning") approaches, which include both statistical and neural networks, on the other hand, have many advantages over the symbolic approach: 

  * both statistical and neural networks methods can focus more on the most common cases extracted from a corpus of texts, whereas the rule-based approach needs to provide rules for both rare cases and common ones equally.

  * [language models](/wiki/Language_model "Language model"), produced by either statistical or neural networks methods, are more robust to both unfamiliar (e.g. containing words or structures that have not been seen before) and erroneous input (e.g. with misspelled words or words accidentally omitted) in comparison to the rule-based systems, which are also more costly to produce.

  * the larger such a (probabilistic) language model is, the more accurate it becomes, in contrast to rule-based systems that can gain accuracy only by increasing the amount and complexity of the rules leading to [intractability](/wiki/Intractable_problem "Intractable problem") problems.

Rule-based systems are commonly used: 

  * when the amount of training data is insufficient to successfully apply machine learning methods, e.g., for the machine translation of low-resource languages such as provided by the [Apertium](/wiki/Apertium "Apertium") system,
  * for preprocessing in NLP pipelines, e.g., [tokenization](/wiki/Tokenization_\(lexical_analysis\) "Tokenization \(lexical analysis\)"), or
  * for postprocessing and transforming the output of NLP pipelines, e.g., for [knowledge extraction](/wiki/Knowledge_extraction "Knowledge extraction") from syntactic parses.

### Statistical approach

[[edit](/w/index.php?title=Natural_language_processing&action=edit&section=5 "Edit section: Statistical approach")]

In the late 1980s and mid-1990s, the statistical approach ended a period of [AI winter](/wiki/AI_winter "AI winter"), which was caused by the inefficiencies of the rule-based approaches.[[21]](#cite_note-johnson:eacl:ilcl09-21)[[22]](#cite_note-resnik:langlog11-22)

The earliest [decision trees](/wiki/Decision_tree "Decision tree"), producing systems of hard [if–then rules](/wiki/Conditional_\(computer_programming\)#If–then\(–else\) "Conditional \(computer programming\)"), were still very similar to the old rule-based approaches. Only the introduction of hidden [Markov models](/wiki/Markov_model "Markov model"), applied to part-of-speech tagging, announced the end of the old rule-based approach. 

### Neural networks

[[edit](/w/index.php?title=Natural_language_processing&action=edit&section=6 "Edit section: Neural networks")]

Further information: [Artificial neural network](/wiki/Artificial_neural_network "Artificial neural network")

A major drawback of statistical methods is that they require elaborate [feature engineering](/wiki/Feature_engineering "Feature engineering"). Since 2015,[[23]](#cite_note-23) the statistical approach has been replaced by the [neural networks](/wiki/Artificial_neural_network "Artificial neural network") approach, using [semantic networks](/wiki/Semantic_networks "Semantic networks")[[24]](#cite_note-24) and [word embeddings](/wiki/Word_embedding "Word embedding") to capture semantic properties of words. 

Intermediate tasks (e.g., part-of-speech tagging and dependency parsing) are not needed anymore. 

[Neural machine translation](/wiki/Neural_machine_translation "Neural machine translation"), based on then-newly invented [sequence-to-sequence](/wiki/Seq2seq "Seq2seq") transformations, made obsolete the intermediate steps, such as word alignment, previously necessary for [statistical machine translation](/wiki/Statistical_machine_translation "Statistical machine translation"). 

## Common NLP tasks

[[edit](/w/index.php?title=Natural_language_processing&action=edit&section=7 "Edit section: Common NLP tasks")]

The following is a list of some of the most commonly researched tasks in natural language processing. Some of these tasks have direct real-world applications, while others more commonly serve as subtasks that are used to aid in solving larger tasks. 

Though natural language processing tasks are closely intertwined, they can be subdivided into categories for convenience. A coarse division is given below. 

### Text and speech processing

[[edit](/w/index.php?title=Natural_language_processing&action=edit&section=8 "Edit section: Text and speech processing")]

[![](//upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Hebrew_stop_words_word_cloud.png/250px-Hebrew_stop_words_word_cloud.png)](/wiki/File:Hebrew_stop_words_word_cloud.png)Word cloud of stop words in Hebrew

[Optical character recognition](/wiki/Optical_character_recognition "Optical character recognition") (OCR)
    Given an image representing printed text, determine the corresponding text.

[Speech recognition](/wiki/Speech_recognition "Speech recognition")
    Given a sound clip of a person or people speaking, determine the textual representation of the speech. This is the opposite of [text to speech](/wiki/Text_to_speech "Text to speech") and is one of the extremely difficult problems colloquially termed "[AI-complete](/wiki/AI-complete "AI-complete")" (see above). In [natural speech](/wiki/Natural_speech "Natural speech") there are hardly any pauses between successive words, and thus [speech segmentation](/wiki/Speech_segmentation "Speech segmentation") is a necessary subtask of speech recognition (see below). In most spoken languages, the sounds representing successive letters blend into each other in a process termed [coarticulation](/wiki/Coarticulation "Coarticulation"), so the conversion of the [analog signal](/wiki/Analog_signal "Analog signal") to discrete characters can be a very difficult process. Also, given that words in the same language are spoken by people with different accents, the speech recognition software must be able to recognize the wide variety of input as being identical to each other in terms of its textual equivalent.
[Speech segmentation](/wiki/Speech_segmentation "Speech segmentation")
    Given a sound clip of a person or people speaking, separate it into words. A subtask of [speech recognition](/wiki/Speech_recognition "Speech recognition") and typically grouped with it.

[Text-to-speech](/wiki/Text-to-speech "Text-to-speech")
    Given a text, transform those units and produce a spoken representation. Text-to-speech can be used to aid the visually impaired.[[25]](#cite_note-25)

[Word segmentation](/wiki/Word_segmentation "Word segmentation") ([Tokenization](/wiki/Tokenization_\(lexical_analysis\) "Tokenization \(lexical analysis\)"))
    Tokenization is a process used in text analysis that divides text into individual words or word fragments. This technique results in two key components: a word index and tokenized text. The word index is a list that maps unique words to specific numerical identifiers, and the tokenized text replaces each word with its corresponding numerical token. These numerical tokens are then used in various deep learning methods.[[26]](#cite_note-:0-26)
    For a language like [English](/wiki/English_language "English language"), this is fairly trivial, since words are usually separated by spaces. However, some written languages like [Chinese](/wiki/Chinese_language "Chinese language"), [Japanese](/wiki/Japanese_language "Japanese language") and [Thai](/wiki/Thai_language "Thai language") do not mark word boundaries in such a fashion, and in those languages text segmentation is a significant task requiring knowledge of the [vocabulary](/wiki/Vocabulary "Vocabulary") and [morphology](/wiki/Morphology_\(linguistics\) "Morphology \(linguistics\)") of words in the language. Sometimes this process is also used in cases like [bag of words](/wiki/Bag_of_words "Bag of words") (BOW) creation in data mining.[_[citation needed](/wiki/Wikipedia:Citation_needed "Wikipedia:Citation needed")_]

### Morphological analysis

[[edit](/w/index.php?title=Natural_language_processing&action=edit&section=9 "Edit section: Morphological analysis")]

[![](//upload.wikimedia.org/wikipedia/commons/thumb/2/27/Eustagger_euskal_lematizatzailearen_adibidea.png/250px-Eustagger_euskal_lematizatzailearen_adibidea.png)](/wiki/File:Eustagger_euskal_lematizatzailearen_adibidea.png)Lemmatization of Basque words

[Lemmatization](/wiki/Lemmatisation "Lemmatisation")
    The task of removing inflectional endings only and to return the base dictionary form of a word which is also known as a lemma. Lemmatization is another technique for reducing words to their normalized form. But in this case, the transformation actually uses a dictionary to map words to their actual form.[[27]](#cite_note-27)
[Morphological segmentation](/wiki/Morphology_\(linguistics\) "Morphology \(linguistics\)")
    Separate words into individual [morphemes](/wiki/Morpheme "Morpheme") and identify the class of the morphemes. The difficulty of this task depends greatly on the complexity of the [morphology](/wiki/Morphology_\(linguistics\) "Morphology \(linguistics\)") (_i.e._ , the structure of words) of the language being considered. [English](/wiki/English_language "English language") has fairly simple morphology, especially [inflectional morphology](/wiki/Inflectional_morphology "Inflectional morphology"), and thus it is often possible to ignore this task entirely and simply model all possible forms of a word (e.g., "open, opens, opened, opening") as separate words. In languages such as [Turkish](/wiki/Turkish_language "Turkish language") or [Meitei](/wiki/Meitei_language "Meitei language"), a highly [agglutinated](/wiki/Agglutination "Agglutination") Indian language, however, such an approach is not possible, as each dictionary entry has thousands of possible word forms.[[28]](#cite_note-28)
[Part-of-speech tagging](/wiki/Part-of-speech_tagging "Part-of-speech tagging")
    Given a sentence, determine the [part of speech](/wiki/Part_of_speech "Part of speech") (POS) for each word. Many words, especially common ones, can serve as multiple parts of speech. For example, "book" can be a [noun](/wiki/Noun "Noun") ("the book on the table") or [verb](/wiki/Verb "Verb") ("to book a flight"); "set" can be a noun, verb or [adjective](/wiki/Adjective "Adjective"); and "out" can be any of at least five different parts of speech.

[Stemming](/wiki/Stemming "Stemming")
    The process of reducing inflected (or sometimes derived) words to a base form (e.g., "close" will be the root for "closed", "closing", "close", "closer" etc.). Stemming yields similar results as lemmatization, but does so on grounds of rules, not a dictionary.

### Syntactic analysis

[[edit](/w/index.php?title=Natural_language_processing&action=edit&section=10 "Edit section: Syntactic analysis")]

Part of [_a series_](/wiki/Category:Formal_languages "Category:Formal languages") on  
---  
[Formal languages](/wiki/Formal_languages "Formal languages")  
Key concepts

  * [Formal system](/wiki/Formal_system "Formal system")
  * [Alphabet](/wiki/Alphabet_\(formal_languages\) "Alphabet \(formal languages\)")
  * [Syntax](/wiki/Syntax_\(logic\) "Syntax \(logic\)")
  * [Formal semantics](/wiki/Semantics_of_logic "Semantics of logic")
  * [Semantics (programming languages)](/wiki/Semantics_\(computer_science\) "Semantics \(computer science\)")
  * [Formal grammar](/wiki/Formal_grammar "Formal grammar")
  * [Formation rule](/wiki/Formation_rule "Formation rule")
  * [Well-formed formula](/wiki/Well-formed_formula "Well-formed formula")
  * [Automata theory](/wiki/Automata_theory "Automata theory")
  * [Regular expression](/wiki/Regular_expression "Regular expression")
  * [Production](/wiki/Production_\(computer_science\) "Production \(computer science\)")
  * [Ground expression](/wiki/Ground_expression "Ground expression")
  * [Atomic formula](/wiki/Atomic_formula "Atomic formula")

  
Applications

  * [Formal methods](/wiki/Formal_methods "Formal methods")
  * [Propositional calculus](/wiki/Propositional_calculus "Propositional calculus")
  * [Predicate logic](/wiki/Predicate_logic "Predicate logic")
  * [Mathematical notation](/wiki/Mathematical_notation "Mathematical notation")
  * Natural language processing
  * [Programming language theory](/wiki/Programming_language_theory "Programming language theory")
  * [Mathematical linguistics](/wiki/Mathematical_linguistics "Mathematical linguistics")
  * [Computational linguistics](/wiki/Computational_linguistics "Computational linguistics")
  * [Syntax analysis](/wiki/Syntax_analysis "Syntax analysis")
  * [Formal verification](/wiki/Formal_verification "Formal verification")
  * [Automated theorem proving](/wiki/Automated_theorem_proving "Automated theorem proving")

  
  
  * [v](/wiki/Template:Formal_languages "Template:Formal languages")
  * [t](/w/index.php?title=Template_talk:Formal_languages&action=edit&redlink=1 "Template talk:Formal languages \(page does not exist\)")
  * [e](/wiki/Special:EditPage/Template:Formal_languages "Special:EditPage/Template:Formal languages")

  
  
[Grammar induction](/wiki/Grammar_induction "Grammar induction")[[29]](#cite_note-29)
    Generate a [formal grammar](/wiki/Formal_grammar "Formal grammar") that describes a language's syntax.
[Sentence breaking](/wiki/Sentence_breaking "Sentence breaking") (also known as "[sentence boundary disambiguation](/wiki/Sentence_boundary_disambiguation "Sentence boundary disambiguation")")
    Given a chunk of text, find the sentence boundaries. Sentence boundaries are often marked by [periods](/wiki/Full_stop "Full stop") or other [punctuation marks](/wiki/Punctuation_mark "Punctuation mark"), but these same characters can serve other purposes (e.g., marking [abbreviations](/wiki/Abbreviation "Abbreviation")).
[Parsing](/wiki/Parsing "Parsing")
    Determine the [parse tree](/wiki/Parse_tree "Parse tree") (grammatical analysis) of a given sentence. The [grammar](/wiki/Grammar "Grammar") for [natural languages](/wiki/Natural_language "Natural language") is [ambiguous](/wiki/Ambiguous "Ambiguous") and typical sentences have multiple possible analyses: perhaps surprisingly, for a typical sentence there may be thousands of potential parses (most of which will seem completely nonsensical to a human). There are two primary types of parsing: _dependency parsing_ and _constituency parsing_. Dependency parsing focuses on the relationships between words in a sentence (marking things like primary objects and predicates), whereas constituency parsing focuses on building out the parse tree using a [probabilistic context-free grammar](/wiki/Probabilistic_context-free_grammar "Probabilistic context-free grammar") (PCFG) (see also _[stochastic grammar](/wiki/Stochastic_grammar "Stochastic grammar")_).

### Lexical semantics (of individual words in context)

[[edit](/w/index.php?title=Natural_language_processing&action=edit&section=11 "Edit section: Lexical semantics \(of individual words in context\)")]

[![](//upload.wikimedia.org/wikipedia/commons/thumb/3/34/Entity_Linking_-_Example_of_pipeline.png/250px-Entity_Linking_-_Example_of_pipeline.png)](/wiki/File:Entity_Linking_-_Example_of_pipeline.png)An entity linking pipeline

[Lexical semantics](/wiki/Lexical_semantics "Lexical semantics")
    What is the computational meaning of individual words in context?
[Distributional semantics](/wiki/Distributional_semantics "Distributional semantics")
    How can we learn semantic representations from data?
[Named entity recognition](/wiki/Named_entity_recognition "Named entity recognition") (NER)
    Given a stream of text, determine which items in the text map to proper names, such as people or places, and what the type of each such name is (e.g. person, location, organization). Although [capitalization](/wiki/Capitalization "Capitalization") can aid in recognizing named entities in languages such as English, this information cannot aid in determining the type of [named entity](/wiki/Named_entity "Named entity"), and in any case, is often inaccurate or insufficient. For example, the first letter of a sentence is also capitalized, and named entities often span several words, only some of which are capitalized. Furthermore, many other languages in non-Western scripts (e.g. [Chinese](/wiki/Chinese_language "Chinese language") or [Arabic](/wiki/Arabic_language "Arabic language")) do not have any capitalization at all, and even languages with capitalization may not consistently use it to distinguish names. For example, [German](/wiki/German_language "German language") capitalizes all [nouns](/wiki/Noun "Noun"), regardless of whether they are names, and [French](/wiki/French_language "French language") and [Spanish](/wiki/Spanish_language "Spanish language") do not capitalize names that serve as [adjectives](/wiki/Adjective "Adjective"). Another name for this task is token classification.[[30]](#cite_note-30)

[Sentiment analysis](/wiki/Sentiment_analysis "Sentiment analysis") (see also [Multimodal sentiment analysis](/wiki/Multimodal_sentiment_analysis "Multimodal sentiment analysis"))
    Sentiment analysis is a computational method used to identify and classify the emotional intent behind text. This technique involves analyzing text to determine whether the expressed sentiment is positive, negative, or neutral. Models for sentiment classification typically utilize inputs such as [word n-grams](/wiki/Word_n-gram_language_model "Word n-gram language model"), [Term Frequency-Inverse Document Frequency](/wiki/Term_frequency-inverse_document_frequency "Term frequency-inverse document frequency") (TF-IDF) features, hand-generated features, or employ [deep learning](/wiki/Deep_learning "Deep learning") models designed to recognize both long-term and short-term dependencies in text sequences. The applications of sentiment analysis are diverse, extending to tasks such as categorizing customer reviews on various online platforms.[[26]](#cite_note-:0-26)
[Terminology extraction](/wiki/Terminology_extraction "Terminology extraction")
    The goal of terminology extraction is to automatically extract relevant terms from a given corpus.
[Word-sense disambiguation](/wiki/Word-sense_disambiguation "Word-sense disambiguation") (WSD)
    Many words have more than one [meaning](/wiki/Meaning_\(linguistics\) "Meaning \(linguistics\)"); we have to select the meaning which makes the most sense in context. For this problem, we are typically given a list of words and associated word senses, e.g. from a dictionary or an online resource such as [WordNet](/wiki/WordNet "WordNet").
[Entity linking](/wiki/Entity_linking "Entity linking")
    Many words—typically proper names—refer to [named entities](/wiki/Named_entity "Named entity"); here we have to select the entity (a famous individual, a location, a company, etc.) which is referred to in context.

### Relational semantics (semantics of individual sentences)

[[edit](/w/index.php?title=Natural_language_processing&action=edit&section=12 "Edit section: Relational semantics \(semantics of individual sentences\)")]

[Relationship extraction](/wiki/Relationship_extraction "Relationship extraction")
    Given a chunk of text, identify the relationships among named entities (e.g. who is married to whom).
[Semantic parsing](/wiki/Semantic_parsing "Semantic parsing")
    Given a piece of text (typically a sentence), produce a formal representation of its semantics, either as a graph (e.g., in [AMR parsing](/wiki/Abstract_Meaning_Representation "Abstract Meaning Representation")) or in accordance with a logical formalism (e.g., in [DRT parsing](/wiki/Discourse_representation_theory "Discourse representation theory")). This challenge typically includes aspects of several more elementary NLP tasks from semantics (e.g., semantic role labelling, word-sense disambiguation) and can be extended to include full-fledged discourse analysis (e.g., discourse analysis, coreference; see [Natural language understanding](#Natural_language_understanding) below).
[Semantic role labelling](/wiki/Semantic_role_labeling "Semantic role labeling") (see also implicit semantic role labelling below)
    Given a single sentence, identify and disambiguate semantic predicates (e.g., verbal [frames](/wiki/Frame_semantics_\(linguistics\) "Frame semantics \(linguistics\)")), then identify and classify the frame elements ([semantic roles](/wiki/Semantic_roles "Semantic roles")).

### Discourse (semantics beyond individual sentences)

[[edit](/w/index.php?title=Natural_language_processing&action=edit&section=13 "Edit section: Discourse \(semantics beyond individual sentences\)")]

[Coreference resolution](/wiki/Coreference "Coreference")
    Given a sentence or larger chunk of text, determine which words ("mentions") refer to the same objects ("entities"). [Anaphora resolution](/wiki/Anaphora_resolution "Anaphora resolution") is a specific example of this task, and is specifically concerned with matching up [pronouns](/wiki/Pronoun "Pronoun") with the nouns or names to which they refer. The more general task of coreference resolution also includes identifying so-called "bridging relationships" involving [referring expressions](/wiki/Referring_expression "Referring expression"). For example, in a sentence such as "He entered John's house through the front door", "the front door" is a referring expression and the bridging relationship to be identified is the fact that the door being referred to is the front door of John's house (rather than of some other structure that might also be referred to).
[Discourse analysis](/wiki/Discourse_analysis "Discourse analysis")
    This rubric includes several related tasks. One task is discourse parsing, i.e., identifying the [discourse](/wiki/Discourse "Discourse") structure of a connected text, i.e. the nature of the discourse relationships between sentences (e.g. elaboration, explanation, contrast). Another possible task is recognizing and classifying the [speech acts](/wiki/Speech_act "Speech act") in a chunk of text (e.g. yes–no question, content question, statement, assertion, etc.).

Implicit semantic role labelling
    Given a single sentence, identify and disambiguate semantic predicates (e.g., verbal [frames](/wiki/Frame_semantics_\(linguistics\) "Frame semantics \(linguistics\)")) and their explicit semantic roles in the current sentence (see [Semantic role labelling](#Semantic_role_labelling) above). Then, identify semantic roles that are not explicitly realized in the current sentence, classify them into arguments that are explicitly realized elsewhere in the text and those that are not specified, and resolve the former against the local text. A closely related task is zero anaphora resolution, i.e., the extension of coreference resolution to [pro-drop languages](/wiki/Pro-drop_language "Pro-drop language").

[Recognizing textual entailment](/wiki/Textual_entailment "Textual entailment")
    Given two text fragments, determine if one being true entails the other, entails the other's negation, or allows the other to be either true or false.[[31]](#cite_note-rte:11-31)

[Topic segmentation](/wiki/Topic_segmentation "Topic segmentation") and recognition
    Given a chunk of text, separate it into segments each of which is devoted to a topic, and identify the topic of the segment.

[Argument mining](/wiki/Argument_mining "Argument mining")
    The goal of argument mining is the automatic extraction and identification of argumentative structures from [natural language](/wiki/Natural_language "Natural language") text with the aid of computer programs.[[32]](#cite_note-32) Such argumentative structures include the premise, conclusions, the [argument scheme](/wiki/Argument_scheme "Argument scheme") and the relationship between the main and subsidiary argument, or the main and counter-argument within discourse.[[33]](#cite_note-33)[[34]](#cite_note-34)

### Higher-level NLP applications

[[edit](/w/index.php?title=Natural_language_processing&action=edit&section=14 "Edit section: Higher-level NLP applications")]

[![](//upload.wikimedia.org/wikipedia/commons/thumb/4/43/Use_of_Firefox%27_%27Translate_selection_to_English%27_machine_translation_on_Commons_talk_meta_pages_02.png/250px-Use_of_Firefox%27_%27Translate_selection_to_English%27_machine_translation_on_Commons_talk_meta_pages_02.png)](/wiki/File:Use_of_Firefox%27_%27Translate_selection_to_English%27_machine_translation_on_Commons_talk_meta_pages_02.png)Machine translation in Firefox

[Automatic summarization](/wiki/Automatic_summarization "Automatic summarization") (text summarization)
    Produce a readable summary of a chunk of text. Often used to provide summaries of the text of a known type, such as research papers, articles in the financial section of a newspaper.
Grammatical error correction
    Grammatical error detection and correction involves a great band-width of problems on all levels of linguistic analysis (phonology/orthography, morphology, syntax, semantics, pragmatics). Grammatical error correction is impactful since it affects hundreds of millions of people that use or acquire English as a second language. It has thus been subject to a number of shared tasks since 2011.[[35]](#cite_note-35)[[36]](#cite_note-36)[[37]](#cite_note-37) As far as orthography, morphology, syntax and certain aspects of semantics are concerned, and due to the development of powerful neural language models such as [GPT-2](/wiki/GPT-2 "GPT-2"), this can now (2019) be considered a largely solved problem and is being marketed in various commercial applications.
[Logic translation](/wiki/Logic_translation "Logic translation")
    Translate a text from a natural language into formal logic.
[Machine translation](/wiki/Machine_translation "Machine translation") (MT)
    Automatically translate text from one human language to another. This is one of the most difficult problems, and is a member of a class of problems colloquially termed "[AI-complete](/wiki/AI-complete "AI-complete")", i.e. requiring all of the different types of knowledge that humans possess (grammar, semantics, facts about the real world, etc.) to solve properly.
[Natural language understanding](/wiki/Natural_language_understanding "Natural language understanding") (NLU)
    Convert chunks of text into more formal representations such as [first-order logic](/wiki/First-order_logic "First-order logic") structures that are easier for [computer](/wiki/Computer "Computer") programs to manipulate. Natural language understanding involves the identification of the intended semantic from the multiple possible semantics which can be derived from a natural language expression which usually takes the form of organized notations of natural language concepts. Introduction and creation of language metamodel and ontology are efficient however empirical solutions. An explicit formalization of natural language semantics without confusions with implicit assumptions such as [closed-world assumption](/wiki/Closed-world_assumption "Closed-world assumption") (CWA) vs. [open-world assumption](/wiki/Open-world_assumption "Open-world assumption"), or subjective Yes/No vs. objective True/False is expected for the construction of a basis of semantics formalization.[[38]](#cite_note-38)
[Natural language generation](/wiki/Natural_language_generation "Natural language generation") (NLG):
    Convert information from computer databases or semantic intents into readable human language.
Book generation
    Not an NLP task proper but an extension of natural language generation and other NLP tasks is the creation of full-fledged books. The first machine-generated book was created by a rule-based system in 1984 (Racter, _The policeman's beard is half-constructed_).[[39]](#cite_note-39) The first published work by a neural network was published in 2018, _[1 the Road](/wiki/1_the_Road "1 the Road")_ , marketed as a novel, contains sixty million words. Both these systems are basically elaborate but non-sensical (semantics-free) [language models](/wiki/Language_model "Language model"). The first machine-generated science book was published in 2019 (Beta Writer, _Lithium-Ion Batteries_ , Springer, Cham).[[40]](#cite_note-40) Unlike _Racter_ and _1 the Road_ , this is grounded on factual knowledge and based on text summarization.
[Document AI](/wiki/Document_AI "Document AI")
    A Document AI platform sits on top of the NLP technology enabling users with no prior experience of artificial intelligence, machine learning or NLP to quickly train a computer to extract the specific data they need from different document types. NLP-powered Document AI enables non-technical teams to quickly access information hidden in documents, for example, lawyers, business analysts and accountants.[[41]](#cite_note-41)
[Dialogue management](/wiki/Dialogue_system "Dialogue system")
    Computer systems intended to converse with a human.
[Question answering](/wiki/Question_answering "Question answering")
    Given a human-language question, determine its answer. Typical questions have a specific right answer (such as "What is the capital of Canada?"), but sometimes open-ended questions are also considered (such as "What is the meaning of life?").
[Text-to-image generation](/wiki/Text-to-image_generation "Text-to-image generation")
    Given a description of an image, generate an image that matches the description.[[42]](#cite_note-42)
Text-to-scene generation
    Given a description of a scene, generate a [3D model](/wiki/3D_model "3D model") of the scene.[[43]](#cite_note-43)[[44]](#cite_note-44)
[Text-to-video](/wiki/Text-to-video_model "Text-to-video model")
    Given a description of a video, generate a video that matches the description.[[45]](#cite_note-45)[[46]](#cite_note-46)

## General tendencies and (possible) future directions

[[edit](/w/index.php?title=Natural_language_processing&action=edit&section=15 "Edit section: General tendencies and \(possible\) future directions")]

Based on long-standing trends in the field, it is possible to extrapolate future directions of NLP. As of 2020, three trends among the topics of the long-standing series of CoNLL Shared Tasks can be observed:[[47]](#cite_note-47)

  * Interest on increasingly abstract, "cognitive" aspects of natural language (1999–2001: shallow parsing, 2002–03: named entity recognition, 2006–09/2017–18: dependency syntax, 2004–05/2008–09 semantic role labelling, 2011–12 coreference, 2015–16: discourse parsing, 2019: semantic parsing).
  * Increasing interest in multilinguality, and, potentially, multimodality (English since 1999; Spanish, Dutch since 2002; German since 2003; Bulgarian, Danish, Japanese, Portuguese, Slovenian, Swedish, Turkish since 2006; Basque, Catalan, Chinese, Greek, Hungarian, Italian, Turkish since 2007; Czech since 2009; Arabic since 2012; 2017: 40+ languages; 2018: 60+/100+ languages)
  * Elimination of symbolic representations (rule-based over supervised towards weakly supervised methods, representation learning and end-to-end systems)

### Cognition

[[edit](/w/index.php?title=Natural_language_processing&action=edit&section=16 "Edit section: Cognition")]

Most higher-level NLP applications involve aspects that emulate intelligent behaviour and apparent comprehension of natural language. More broadly speaking, the technical operationalization of increasingly advanced aspects of cognitive behaviour represents one of the developmental trajectories of NLP (see trends among CoNLL shared tasks above). 

[Cognition](/wiki/Cognition "Cognition") refers to "the mental action or process of acquiring knowledge and understanding through thought, experience, and the senses."[[48]](#cite_note-48) [Cognitive science](/wiki/Cognitive_science "Cognitive science") is the interdisciplinary, scientific study of the mind and its processes.[[49]](#cite_note-49) [Cognitive linguistics](/wiki/Cognitive_linguistics "Cognitive linguistics") is an interdisciplinary branch of linguistics, combining knowledge and research from both psychology and linguistics.[[50]](#cite_note-50) Especially during the age of [symbolic NLP](#Symbolic_NLP_\(1950s_–_early_1990s\)), the area of computational linguistics maintained strong ties with cognitive studies. 

As an example, [George Lakoff](/wiki/George_Lakoff "George Lakoff") offers a methodology to build natural language processing (NLP) algorithms through the perspective of cognitive science, along with the findings of cognitive linguistics,[[51]](#cite_note-51) with two defining aspects: 

  1. Apply the theory of [conceptual metaphor](/wiki/Conceptual_metaphor "Conceptual metaphor"), explained by Lakoff as "the understanding of one idea, in   2. Assign relative measures of meaning to a word, phrase, sentence or piece of text based on the information presented before and after the piece of text being analyzed, e.g., by means of a [probabilistic context-free grammar](/wiki/Probabilistic_context-free_grammar "Probabilistic context-free grammar") (PCFG). The mathematical equation for such algorithms is presented in [US Patent 9269353](https://worldwide.espacenet.com/patent/search/family/055314712/publication/US9269353B1?q=pn%3DUS9269353) [Archived](https://web.archive.org/web/20240516102600/https://worldwide.espacenet.com/patent/search/family/055314712/publication/US9269353B1?q=pn=US9269353) 2024-05-16 at the [Wayback Machine](/wiki/Wayback_Machine "Wayback Machine"):[[53]](#cite_note-53)

    

     R M M ( t o k e n N ) = P M M ( t o k e n N ) × 1 2 d ( ∑ i = − d d ( ( P M M ( t o k e n N ) × P F ( t o k e n N − i , t o k e n N , t o k e n N + i ) ) i ) {\displaystyle {RMM(token_{N})}={PMM(token_{N})}\times {\frac {1}{2d}}\left(\sum _{i=-d}^{d}{((PMM(token_{N})}\times {PF(token_{N-i},token_{N},token_{N+i}))_{i}}\right)} ![{\\displaystyle {RMM\(token_{N}\)}={PMM\(token_{N}\)}\\times {\\frac {1}{2d}}\\left\(\\sum _{i=-d}^{d}{\(\(PMM\(token_{N}\)}\\times {PF\(token_{N-i},token_{N},token_{N+i}\)\)_{i}}\\right\)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/43ccadd794a4b84e20d1209997a463342e0dfbfe)

    

    _Where_

    **RMM** is the relative measure of meaning
    **token** is any block of text, sentence, phrase or word
    **N** is the number of tokens being analyzed
    **PMM** is the probable measure of meaning based on a corpora
    **d** is the non zero location of the token along the sequence of **N** tokens
    **PF** is the probability function specific to a language

Ties with cognitive linguistics are part of the historical heritage of NLP, but they have been less frequently addressed since the statistical turn during the 1990s. Nevertheless, approaches to develop cognitive models towards technically operationalizable frameworks have been pursued in the context of various frameworks, e.g., of cognitive grammar,[[54]](#cite_note-54) functional grammar,[[55]](#cite_note-55) construction grammar,[[56]](#cite_note-56) computational psycholinguistics and cognitive neuroscience (e.g., [ACT-R](/wiki/ACT-R "ACT-R")), however, with limited uptake in mainstream NLP (as measured by presence on major conferences[[57]](#cite_note-57) of the [ACL](/wiki/Association_for_Computational_Linguistics "Association for Computational Linguistics")). More recently, ideas of cognitive NLP have been revived as an approach to achieve [explainability](/wiki/Explainable_artificial_intelligence "Explainable artificial intelligence"), e.g., under the notion of "cognitive AI".[[58]](#cite_note-58) Likewise, ideas of cognitive NLP are inherent to neural models [multimodal](/wiki/Multimodal_interaction "Multimodal interaction") NLP (although rarely made explicit)[[59]](#cite_note-59) and developments in [artificial intelligence](/wiki/Artificial_intelligence "Artificial intelligence"), specifically tools and technologies using [large language model](/wiki/Large_language_model "Large language model") approaches[[60]](#cite_note-60) and new directions in [artificial general intelligence](/wiki/Artificial_general_intelligence "Artificial general intelligence") based on the [free energy principle](/wiki/Free_energy_principle "Free energy principle")[[61]](#cite_note-61) by British neuroscientist and theoretician at University College London [Karl J. Friston](/wiki/Karl_J._Friston "Karl J. Friston"). 

## See also

[[edit](/w/index.php?title=Natural_language_processing&action=edit&section=17 "Edit section: See also")]

  * _[1 the Road](/wiki/1_the_Road "1 the Road")_
  * [Artificial intelligence detection software](/wiki/Artificial_intelligence_detection_software "Artificial intelligence detection software")
  * [Automated essay scoring](/wiki/Automated_essay_scoring "Automated essay scoring")
  * [Biomedical text mining](/wiki/Biomedical_text_mining "Biomedical text mining")
  * [Compound term processing](/wiki/Compound_term_processing "Compound term processing")
  * [Computational linguistics](/wiki/Computational_linguistics "Computational linguistics")
  * [Computer-assisted reviewing](/wiki/Computer-assisted_reviewing "Computer-assisted reviewing")
  * [Controlled natural language](/wiki/Controlled_natural_language "Controlled natural language")
  * [Deep learning](/wiki/Deep_learning "Deep learning")
  * [Deep linguistic processing](/wiki/Deep_linguistic_processing "Deep linguistic processing")
  * [Distributional semantics](/wiki/Distributional_semantics "Distributional semantics")
  * [Foreign language reading aid](/wiki/Foreign_language_reading_aid "Foreign language reading aid")
  * [Foreign language writing aid](/wiki/Foreign_language_writing_aid "Foreign language writing aid")
  * [Information extraction](/wiki/Information_extraction "Information extraction")
  * [Information retrieval](/wiki/Information_retrieval "Information retrieval")
  * [Language and Communication Technologies](/wiki/Language_and_Communication_Technologies "Language and Communication Technologies")
  * [Language model](/wiki/Language_model "Language model")
  * [Language technology](/wiki/Language_technology "Language technology")
  * [Latent semantic indexing](/wiki/Latent_semantic_indexing "Latent semantic indexing")
  * [Multi-agent system](/wiki/Multi-agent_system "Multi-agent system")
  * [Native-language identification](/wiki/Native-language_identification "Native-language identification")
  * [Natural-language programming](/wiki/Natural-language_programming "Natural-language programming")
  * [Natural-language understanding](/wiki/Natural-language_understanding "Natural-language understanding")
  * [Natural-language search](/wiki/Natural-language_user_interface "Natural-language user interface")
  * [Outline of natural language processing](/wiki/Outline_of_natural_language_processing "Outline of natural language processing")
  * [Query expansion](/wiki/Query_expansion "Query expansion")
  * [Query understanding](/wiki/Query_understanding "Query understanding")
  * [Reification (linguistics)](/wiki/Reification_\(linguistics\) "Reification \(linguistics\)")
  * [Speech processing](/wiki/Speech_processing "Speech processing")
  * [Spoken dialogue systems](/wiki/Spoken_dialogue_systems "Spoken dialogue systems")
  * [Text-proofing](/wiki/Text-proofing "Text-proofing")
  * [Text simplification](/wiki/Text_simplification "Text simplification")
  * [Transformer (machine learning model)](/wiki/Transformer_\(machine_learning_model\) "Transformer \(machine learning model\)")
  * [Truecasing](/wiki/Truecasing "Truecasing")
  * [Question answering](/wiki/Question_answering "Question answering")
  * [Word2vec](/wiki/Word2vec "Word2vec")

## References

[[edit](/w/index.php?title=Natural_language_processing&action=edit&section=18 "Edit section: References")]

  1. **[^](#cite_ref-nlpintro_1-0)** Eisenstein, Jacob (October 1, 2019). [_Introduction to Natural Language Processing_](https://mitpress.mit.edu/9780262042840/introduction-to-natural-language-processing/). The MIT Press. p. 1\. [ISBN](/wiki/ISBN_\(identifier\) "ISBN \(identifier\)") [978-0-262-04284-0](/wiki/Special:BookSources/978-0-262-04284-0 "Special:BookSources/978-0-262-04284-0").
  2. **[^](#cite_ref-2)** ["NLP"](https://cs.stanford.edu/people/eroberts/courses/soco/projects/2004-05/nlp/overview_history.html).
  3. **[^](#cite_ref-3)** Hutchins, J. (2005). ["The history of machine translation in a nutshell"](https://web.archive.org/web/20190713103044/http://www.hutchinsweb.me.uk/Nutshell-2005.pdf) (PDF). Archived from [the original](http://www.hutchinsweb.me.uk/Nutshell-2005.pdf) (PDF) on 2019-07-13. Retrieved 2019-02-04.[_[self-published source](/wiki/Wikipedia:Verifiability#Self-published_sources "Wikipedia:Verifiability")_]
  4. **[^](#cite_ref-4)** "ALPAC: the (in)famous report", John Hutchins, MT News International, no. 14, June 1996, pp. 9–12.
  5. **[^](#cite_ref-5)** [Crevier 1993](#CITEREFCrevier1993), pp. 146–148 harvnb error: no target: CITEREFCrevier1993 ([help](/wiki/Category:Harv_and_Sfn_template_errors "Category:Harv and Sfn template errors")), see also [Buchanan 2005](#CITEREFBuchanan2005), p. 56 harvnb error: no target: CITEREFBuchanan2005 ([help](/wiki/Category:Harv_and_Sfn_template_errors "Category:Harv and Sfn template errors")): "Early programs were necessarily limited in scope by the size and speed of memory"
  6. **[^](#cite_ref-6)** [Koskenniemi, Kimmo](/wiki/Kimmo_Koskenniemi "Kimmo Koskenniemi") (1983), [_Two-level morphology: A general computational model of word-form recognition and production_](https://web.archive.org/web/20181221032913/http://www.ling.helsinki.fi/~koskenni/doc/Two-LevelMorphology.pdf) (PDF), Department of General Linguistics, [University of Helsinki](/wiki/University_of_Helsinki "University of Helsinki"), archived from [the original](http://www.ling.helsinki.fi/~koskenni/doc/Two-LevelMorphology.pdf) (PDF) on 2018-12-21, retrieved 2020-08-20
  7. **[^](#cite_ref-7)** Joshi, A. K., & Weinstein, S. (1981, August). [Control of Inference: Role of Some Aspects of Discourse Structure-Centering](https://www.ijcai.org/Proceedings/81-1/Papers/071.pdf). In _IJCAI_ (pp. 385–387).
  8. **[^](#cite_ref-8)** Guida, G.; Mauri, G. (July 1986). "Evaluation of natural language processing systems: Issues and approaches". _Proceedings of the IEEE_. **74** (7): 1026–1035\. [doi](/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.1109/PROC.1986.13580](https://doi.org/10.1109%2FPROC.1986.13580). [ISSN](/wiki/ISSN_\(identifier\) "ISSN \(identifier\)") [1558-2256](https://search.worldcat.org/issn/1558-2256). [S2CID](/wiki/S2CID_\(identifier\) "S2CID \(identifier\)") [30688575](https://api.semanticscholar.org/CorpusID:30688575).
  9. **[^](#cite_ref-9)** Chomskyan linguistics encourages the investigation of "[corner cases](/wiki/Corner_case "Corner case")" that stress the limits of its theoretical models (comparable to [pathological](/wiki/Pathological_\(mathematics\) "Pathological \(mathematics\)") phenomena in mathematics), typically created using [thought experiments](/wiki/Thought_experiment "Thought experiment"), rather than the systematic investigation of typical phenomena that occur in real-world data, as is the case in [corpus linguistics](/wiki/Corpus_linguistics "Corpus linguistics"). The creation and use of such [corpora](/wiki/Text_corpus "Text corpus") of real-world data is a fundamental part of machine-learning algorithms for natural language processing. In addition, theoretical underpinnings of Chomskyan linguistics such as the so-called "[poverty of the stimulus](/wiki/Poverty_of_the_stimulus "Poverty of the stimulus")" argument entail that general learning algorithms, as are typically used in machine learning, cannot be successful in language processing. As a result, the Chomskyan paradigm discouraged the application of such models to language processing.
  10. **[^](#cite_ref-10)** Bengio, Yoshua; Ducharme, Réjean; Vincent, Pascal; Janvin, Christian (March 1, 2003). ["A neural probabilistic language model"](https://dl.acm.org/doi/10.5555/944919.944966). _The Journal of Machine Learning Research_. **3** : 1137–1155 – via ACM Digital Library.
  11. **[^](#cite_ref-11)** Mikolov, Tomáš; Karafiát, Martin; Burget, Lukáš; Černocký, Jan; Khudanpur, Sanjeev (26 September 2010). ["Recurrent neural network based language model"](https://gwern.net/doc/ai/nn/rnn/2010-mikolov.pdf) (PDF). _Interspeech 2010_. pp. 1045–1048\. [doi](/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.21437/Interspeech.2010-343](https://doi.org/10.21437%2FInterspeech.2010-343). [S2CID](/wiki/S2CID_\(identifier\) "S2CID \(identifier\)") [17048224](https://api.semanticscholar.org/CorpusID:17048224). `{{[cite book](/wiki/Template:Cite_book "Template:Cite book")}}`: `|journal=` ignored ([help](/wiki/Help:CS1_errors#periodical_ignored "Help:CS1 errors"))
  12. **[^](#cite_ref-goldberg:nnlp17_12-0)** Goldberg, Yoav (2016). "A Primer on Neural Network Models for Natural Language Processing". _Journal of Artificial Intelligence Research_. **57** : 345–420\. [arXiv](/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[1807.10854](https://arxiv.org/abs/1807.10854). [doi](/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.1613/jair.4992](https://doi.org/10.1613%2Fjair.4992). [S2CID](/wiki/S2CID_\(identifier\) "S2CID \(identifier\)") [8273530](https://api.semanticscholar.org/CorpusID:8273530).
  13. **[^](#cite_ref-goodfellow:book16_13-0)** Goodfellow, Ian; Bengio, Yoshua; Courville, Aaron (2016). [_Deep Learning_](http://www.deeplearningbook.org/). MIT Press.
  14. **[^](#cite_ref-jozefowicz:lm16_14-0)** Jozefowicz, Rafal; Vinyals, Oriol; Schuster, Mike; Shazeer, Noam; Wu, Yonghui (2016). _Exploring the Limits of Language Modeling_. [arXiv](/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[1602.02410](https://arxiv.org/abs/1602.02410). [Bibcode](/wiki/Bibcode_\(identifier\) "Bibcode \(identifier\)"):[2016arXiv160202410J](https://ui.adsabs.harvard.edu/abs/2016arXiv160202410J).
  15. **[^](#cite_ref-choe:emnlp16_15-0)** Choe, Do Kook; Charniak, Eugene. ["Parsing as Language Modeling"](https://web.archive.org/web/20181023034804/https://aclanthology.coli.uni-saarland.de/papers/D16-1257/d16-1257). _Emnlp 2016_. Archived from [the original](https://aclanthology.coli.uni-saarland.de/papers/D16-1257/d16-1257) on 2018-10-23. Retrieved 2018-10-22.
  16. **[^](#cite_ref-vinyals:nips15_16-0)** Vinyals, Oriol; et al. (2014). ["Grammar as a Foreign Language"](https://papers.nips.cc/paper/5635-grammar-as-a-foreign-language.pdf) (PDF). _Nips2015_. [arXiv](/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[1412.7449](https://arxiv.org/abs/1412.7449). [Bibcode](/wiki/Bibcode_\(identifier\) "Bibcode \(identifier\)"):[2014arXiv1412.7449V](https://ui.adsabs.harvard.edu/abs/2014arXiv1412.7449V).
  17. **[^](#cite_ref-17)** Turchin, Alexander; Florez Builes, Luisa F. (2021-03-19). ["Using Natural Language Processing to Measure and Improve Quality of Diabetes Care: A Systematic Review"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8120048). _Journal of Diabetes Science and Technology_. **15** (3): 553–560\. [doi](/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.1177/19322968211000831](https://doi.org/10.1177%2F19322968211000831). [ISSN](/wiki/ISSN_\(identifier\) "ISSN \(identifier\)") [1932-2968](https://search.worldcat.org/issn/1932-2968). [PMC](/wiki/PMC_\(identifier\) "PMC \(identifier\)") [8120048](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8120048). [PMID](/wiki/PMID_\(identifier\) "PMID \(identifier\)") [33736486](https://pubmed.ncbi.nlm.nih.gov/33736486).
  18. **[^](#cite_ref-18)** Lee, Jennifer; Yang, Samuel; Holland-Hall, Cynthia; Sezgin, Emre; Gill, Manjot; Linwood, Simon; Huang, Yungui; Hoffman, Jeffrey (2022-06-10). ["Prevalence of Sensitive Terms in Clinical Notes Using Natural Language Processing Techniques: Observational Study"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9233261). _JMIR Medical Informatics_. **10** (6) e38482. [doi](/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.2196/38482](https://doi.org/10.2196%2F38482). [ISSN](/wiki/ISSN_\(identifier\) "ISSN \(identifier\)") [2291-9694](https://search.worldcat.org/issn/2291-9694). [PMC](/wiki/PMC_\(identifier\) "PMC \(identifier\)") [9233261](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9233261). [PMID](/wiki/PMID_\(identifier\) "PMID \(identifier\)") [35687381](https://pubmed.ncbi.nlm.nih.gov/35687381).
  19. **[^](#cite_ref-winograd:shrdlu71_19-0)** Winograd, Terry (1971). [_Procedures as a Representation for Data in a Computer Program for Understanding Natural Language_](http://hci.stanford.edu/winograd/shrdlu/) (Thesis).
  20. **[^](#cite_ref-schank77_20-0)** Schank, Roger C.; Abelson, Robert P. (1977). _Scripts, Plans, Goals, and Understanding: An Inquiry Into Human Knowledge Structures_. Hillsdale: Erlbaum. [ISBN](/wiki/ISBN_\(identifier\) "ISBN \(identifier\)") [0-470-99033-3](/wiki/Special:BookSources/0-470-99033-3 "Special:BookSources/0-470-99033-3").
  21. **[^](#cite_ref-johnson:eacl:ilcl09_21-0)** [Mark Johnson. How the statistical revolution changes (computational) linguistics.](http://www.aclweb.org/anthology/W09-0103) Proceedings of the EACL 2009 Workshop on the Interaction between Linguistics and Computational Linguistics.
  22. **[^](#cite_ref-resnik:langlog11_22-0)** [Philip Resnik. Four revolutions.](http://languagelog.ldc.upenn.edu/nll/?p=2946) Language Log, February 5, 2011.
  23. **[^](#cite_ref-23)** Socher, Richard. ["Deep Learning For NLP-ACL 2012 Tutorial"](https://web.archive.org/web/20210414054126/https://www.socher.org/index.php/Main/DeepLearningForNLP-ACL2012Tutorial). _www.socher.org_. Archived from [the original](https://www.socher.org/index.php/Main/DeepLearningForNLP-ACL2012Tutorial) on 2021-04-14. Retrieved 2020-08-17. This was an early Deep Learning tutorial at the ACL 2012 and met with both interest and (at the time) skepticism by most participants. Until then, neural learning was basically rejected because of its lack of statistical interpretability. Until 2015, deep learning had evolved into the major framework of NLP. [Link is broken, try <http://web.stanford.edu/class/cs224n/>]
  24. **[^](#cite_ref-24)** Segev, Elad (2022). [_Semantic Network Analysis in Social Sciences_](https://www.routledge.com/Semantic-Network-Analysis-in-Social-Sciences/Segev/p/book/9780367636524). London: Routledge. [ISBN](/wiki/ISBN_\(identifier\) "ISBN \(identifier\)") [978-0-367-63652-4](/wiki/Special:BookSources/978-0-367-63652-4 "Special:BookSources/978-0-367-63652-4"). [Archived](https://web.archive.org/web/20211205140726/https://www.routledge.com/Semantic-Network-Analysis-in-Social-Sciences/Segev/p/book/9780367636524) from the original on 5 December 2021. Retrieved 5 December 2021.
  25. **[^](#cite_ref-25)** Yi, Chucai; [Tian, Yingli](/wiki/Yingli_Tian "Yingli Tian") (2012), "Assistive Text Reading from Complex Background for Blind Persons", _Camera-Based Document Analysis and Recognition_ , Lecture Notes in Computer Science, vol. 7139, Springer Berlin Heidelberg, pp. 15–28, [CiteSeerX](/wiki/CiteSeerX_\(identifier\) "CiteSeerX \(identifier\)") [10.1.1.668.869](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.668.869), [doi](/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.1007/978-3-642-29364-1_2](https://doi.org/10.1007%2F978-3-642-29364-1_2), [ISBN](/wiki/ISBN_\(identifier\) "ISBN \(identifier\)") [978-3-642-29363-4](/wiki/Special:BookSources/978-3-642-29363-4 "Special:BookSources/978-3-642-29363-4")
  26. ^ [_**a**_](#cite_ref-:0_26-0) [_**b**_](#cite_ref-:0_26-1) ["Natural Language Processing (NLP) - A Complete Guide"](https://www.deeplearning.ai/resources/natural-language-processing/). _www.deeplearning.ai_. 2023-01-11. Retrieved 2024-05-05.
  27. **[^](#cite_ref-27)** ["What is Natural Language Processing? Intro to NLP in Machine Learning"](https://www.gyansetu.in/what-is-natural-language-processing/). _GyanSetu!_. 2020-12-06. Retrieved 2021-01-09.
  28. **[^](#cite_ref-28)** Kishorjit, N.; Vidya, Raj RK.; Nirmal, Y.; Sivaji, B. (2012). ["Manipuri Morpheme Identification"](http://aclweb.org/anthology//W/W12/W12-5008.pdf) (PDF). _Proceedings of the 3rd Workshop on South and Southeast Asian Natural Language Processing (SANLP)_. COLING 2012, Mumbai, December 2012: 95–108.`{{[cite journal](/wiki/Template:Cite_journal "Template:Cite journal")}}`: CS1 maint: location ([link](/wiki/Category:CS1_maint:_location "Category:CS1 maint: location"))
  29. **[^](#cite_ref-29)** Klein, Dan; Manning, Christopher D. (2002). ["Natural language grammar induction using a constituent-context model"](http://papers.nips.cc/paper/1945-natural-language-grammar-induction-using-a-constituent-context-model.pdf) (PDF). _Advances in Neural Information Processing Systems_.
  30. **[^](#cite_ref-30)** Kariampuzha, William; Alyea, Gioconda; Qu, Sue; Sanjak, Jaleal; Mathé, Ewy; Sid, Eric; Chatelaine, Haley; Yadaw, Arjun; Xu, Yanji; Zhu, Qian (2023). ["Precision information extraction for rare disease epidemiology at scale"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9972634). _Journal of Translational Medicine_. **21** (1): 157. [doi](/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.1186/s12967-023-04011-y](https://doi.org/10.1186%2Fs12967-023-04011-y). [PMC](/wiki/PMC_\(identifier\) "PMC \(identifier\)") [9972634](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9972634). [PMID](/wiki/PMID_\(identifier\) "PMID \(identifier\)") [36855134](https://pubmed.ncbi.nlm.nih.gov/36855134).
  31. **[^](#cite_ref-rte:11_31-0)** PASCAL Recognizing Textual Entailment Challenge (RTE-7) <https://tac.nist.gov//2011/RTE/>
  32. **[^](#cite_ref-32)** Lippi, Marco; Torroni, Paolo (2016-04-20). ["Argumentation Mining: State of the Art and Emerging Trends"](https://dl.acm.org/doi/10.1145/2850417). _ACM Transactions on Internet Technology_. **16** (2): 1–25\. [doi](/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.1145/2850417](https://doi.org/10.1145%2F2850417). [hdl](/wiki/Hdl_\(identifier\) "Hdl \(identifier\)"):[11585/523460](https://hdl.handle.net/11585%2F523460). [ISSN](/wiki/ISSN_\(identifier\) "ISSN \(identifier\)") [1533-5399](https://search.worldcat.org/issn/1533-5399). [S2CID](/wiki/S2CID_\(identifier\) "S2CID \(identifier\)") [9561587](https://api.semanticscholar.org/CorpusID:9561587).
  33. **[^](#cite_ref-33)** ["Argument Mining – IJCAI2016 Tutorial"](https://web.archive.org/web/20210418083659/https://www.i3s.unice.fr/~villata/tutorialIJCAI2016.html). _www.i3s.unice.fr_. Archived from [the original](https://www.i3s.unice.fr/~villata/tutorialIJCAI2016.html) on 2021-04-18. Retrieved 2021-03-09.
  34. **[^](#cite_ref-34)** ["NLP Approaches to Computational Argumentation – ACL 2016, Berlin"](http://acl2016tutorial.arg.tech/). Retrieved 2021-03-09.
  35. **[^](#cite_ref-35)** Administration. ["Centre for Language Technology (CLT)"](https://www.mq.edu.au/research/research-centres-groups-and-facilities/innovative-technologies/centres/centre-for-language-technology-clt). _Macquarie University_. Retrieved 2021-01-11.
  36. **[^](#cite_ref-36)** ["Shared Task: Grammatical Error Correction"](https://www.comp.nus.edu.sg/~nlp/conll13st.html). _www.comp.nus.edu.sg_. Retrieved 2021-01-11.
  37. **[^](#cite_ref-37)** ["Shared Task: Grammatical Error Correction"](https://www.comp.nus.edu.sg/~nlp/conll14st.html). _www.comp.nus.edu.sg_. Retrieved 2021-01-11.
  38. **[^](#cite_ref-38)** Duan, Yucong; Cruz, Christophe (2011). ["Formalizing Semantic of Natural Language through Conceptualization from Existence"](https://web.archive.org/web/20111009135952/http://www.ijimt.org/abstract/100-E00187.htm). _International Journal of Innovation, Management and Technology_. **2** (1): 37–42\. Archived from [the original](http://www.ijimt.org/abstract/100-E00187.htm) on 2011-10-09.
  39. **[^](#cite_ref-39)** ["U B U W E B :: Racter"](http://www.ubu.com/historical/racter/index.html). _www.ubu.com_. Retrieved 2020-08-17.
  40. **[^](#cite_ref-40)** Writer, Beta (2019). _Lithium-Ion Batteries_. [doi](/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.1007/978-3-030-16800-1](https://doi.org/10.1007%2F978-3-030-16800-1). [ISBN](/wiki/ISBN_\(identifier\) "ISBN \(identifier\)") [978-3-030-16799-8](/wiki/Special:BookSources/978-3-030-16799-8 "Special:BookSources/978-3-030-16799-8"). [S2CID](/wiki/S2CID_\(identifier\) "S2CID \(identifier\)") [155818532](https://api.semanticscholar.org/CorpusID:155818532).
  41. **[^](#cite_ref-41)** ["Document Understanding AI on Google Cloud (Cloud Next '19) – YouTube"](https://ghostarchive.org/varchive/youtube/20211030/7dtl650D0y0). _www.youtube.com_. 11 April 2019. Archived from [the original](https://www.youtube.com/watch?v=7dtl650D0y0) on 2021-10-30. Retrieved 2021-01-11.
  42. **[^](#cite_ref-42)** Robertson, Adi (2022-04-06). ["OpenAI's DALL-E AI image generator can now edit pictures, too"](https://www.theverge.com/2022/4/6/23012123/openai-clip-dalle-2-ai-text-to-image-generator-testing). _The Verge_. Retrieved 2022-06-07.
  43. **[^](#cite_ref-43)** ["The Stanford Natural Language Processing Group"](https://nlp.stanford.edu/projects/text2scene.shtml). _nlp.stanford.edu_. Retrieved 2022-06-07.
  44. **[^](#cite_ref-44)** Coyne, Bob; Sproat, Richard (2001-08-01). ["WordsEye"](https://doi.org/10.1145/383259.383316). _Proceedings of the 28th annual conference on Computer graphics and interactive techniques_. SIGGRAPH '01. New York, NY, USA: Association for Computing Machinery. pp. 487–496\. [doi](/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.1145/383259.383316](https://doi.org/10.1145%2F383259.383316). [ISBN](/wiki/ISBN_\(identifier\) "ISBN \(identifier\)") [978-1-58113-374-5](/wiki/Special:BookSources/978-1-58113-374-5 "Special:BookSources/978-1-58113-374-5"). [S2CID](/wiki/S2CID_\(identifier\) "S2CID \(identifier\)") [3842372](https://api.semanticscholar.org/CorpusID:3842372).
  45. **[^](#cite_ref-45)** ["Google announces AI advances in text-to-video, language translation, more"](https://venturebeat.com/ai/google-announces-ai-advances-in-text-to-video-language-translation-more/). _VentureBeat_. 2022-11-02. Retrieved 2022-11-09.
  46. **[^](#cite_ref-46)** Vincent, James (2022-09-29). ["Meta's new text-to-video AI generator is like DALL-E for video"](https://www.theverge.com/2022/9/29/23378210/meta-text-to-video-ai-generation-make-a-video-model-dall-e). _The Verge_. Retrieved 2022-11-09.
  47. **[^](#cite_ref-47)** ["Previous shared tasks | CoNLL"](https://www.conll.org/previous-tasks). _www.conll.org_. Retrieved 2021-01-11.
  48. **[^](#cite_ref-48)** ["Cognition"](https://web.archive.org/web/20200715113427/https://www.lexico.com/definition/cognition). _Lexico_. [Oxford University Press](/wiki/Oxford_University_Press "Oxford University Press") and [Dictionary.com](/wiki/Dictionary.com "Dictionary.com"). Archived from [the original](https://www.lexico.com/definition/cognition) on July 15, 2020. Retrieved 6 May 2020.
  49. **[^](#cite_ref-49)** ["Ask the Cognitive Scientist"](http://www.aft.org/newspubs/periodicals/ae/summer2002/willingham.cfm). _American Federation of Teachers_. 8 August 2014. "Cognitive science is an interdisciplinary field of researchers from Linguistics, psychology, neuroscience, philosophy, computer science, and anthropology that seek to understand the mind."
  50. **[^](#cite_ref-50)** Robinson, Peter (2008). _Handbook of Cognitive Linguistics and Second Language Acquisition_. Routledge. pp. 3–8\. [ISBN](/wiki/ISBN_\(identifier\) "ISBN \(identifier\)") [978-0-805-85352-0](/wiki/Special:BookSources/978-0-805-85352-0 "Special:BookSources/978-0-805-85352-0").
  51. **[^](#cite_ref-51)** Lakoff, George (1999). _Philosophy in the Flesh: The Embodied Mind and Its Challenge to Western Philosophy; Appendix: The Neural Theory of Language Paradigm_. New York Basic Books. pp. 569–583\. [ISBN](/wiki/ISBN_\(identifier\) "ISBN \(identifier\)") [978-0-465-05674-3](/wiki/Special:BookSources/978-0-465-05674-3 "Special:BookSources/978-0-465-05674-3").
  52. **[^](#cite_ref-52)** Strauss, Claudia (1999). _A Cognitive Theory of Cultural Meaning_. Cambridge University Press. pp. 156–164\. [ISBN](/wiki/ISBN_\(identifier\) "ISBN \(identifier\)") [978-0-521-59541-4](/wiki/Special:BookSources/978-0-521-59541-4 "Special:BookSources/978-0-521-59541-4").
  53. **[^](#cite_ref-53)** [US patent 9269353](https://worldwide.espacenet.com/textdoc?DB=EPODOC&IDX=US9269353)
  54. **[^](#cite_ref-54)** ["Universal Conceptual Cognitive Annotation (UCCA)"](https://universalconceptualcognitiveannotation.github.io/). _Universal Conceptual Cognitive Annotation (UCCA)_. Retrieved 2021-01-11.
  55. **[^](#cite_ref-55)** Rodríguez, F. C., & Mairal-Usón, R. (2016). [Building an RRG computational grammar](https://www.redalyc.org/pdf/1345/134549291020.pdf). _Onomazein_ , (34), 86–117.
  56. **[^](#cite_ref-56)** ["Fluid Construction Grammar – A fully operational processing system for construction grammars"](https://www.fcg-net.org/). Retrieved 2021-01-11.
  57. **[^](#cite_ref-57)** ["ACL Member Portal | The Association for Computational Linguistics Member Portal"](https://www.aclweb.org/portal/). _www.aclweb.org_. Retrieved 2021-01-11.
  58. **[^](#cite_ref-58)** ["Chunks and Rules"](https://www.w3.org/Data/demos/chunks/chunks.html). _W3C_. Retrieved 2021-01-11.
  59. **[^](#cite_ref-59)** Socher, Richard; Karpathy, Andrej; Le, Quoc V.; Manning, Christopher D.; Ng, Andrew Y. (2014). ["Grounded Compositional Semantics for Finding and Describing Images with Sentences"](https://doi.org/10.1162%2Ftacl_a_00177). _Transactions of the Association for Computational Linguistics_. **2** : 207–218\. [doi](/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.1162/tacl_a_00177](https://doi.org/10.1162%2Ftacl_a_00177). [S2CID](/wiki/S2CID_\(identifier\) "S2CID \(identifier\)") [2317858](https://api.semanticscholar.org/CorpusID:2317858).
  60. **[^](#cite_ref-60)** Dasgupta, Ishita; Lampinen, Andrew K.; Chan, Stephanie C. Y.; Creswell, Antonia; Kumaran, Dharshan; McClelland, James L.; Hill, Felix (2022). "Language models show human-like content effects on reasoning, Dasgupta, Lampinen et al". [arXiv](/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[2207.07051](https://arxiv.org/abs/2207.07051) [[cs.CL](https://arxiv.org/archive/cs.CL)].
  61. **[^](#cite_ref-61)** Friston, Karl J. (2022). _Active Inference: The Free Energy Principle in Mind, Brain, and Behavior; Chapter 4 The Generative Models of Active Inference_. The MIT Press. [ISBN](/wiki/ISBN_\(identifier\) "ISBN \(identifier\)") [978-0-262-36997-8](/wiki/Special:BookSources/978-0-262-36997-8 "Special:BookSources/978-0-262-36997-8").

## Further reading

[[edit](/w/index.php?title=Natural_language_processing&action=edit&section=19 "Edit section: Further reading")]

  * Bates, M (1995). ["Models of natural language understanding"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC40721). _Proceedings of the National Academy of Sciences of the United States of America_. **92** (22): 9977–9982\. [Bibcode](/wiki/Bibcode_\(identifier\) "Bibcode \(identifier\)"):[1995PNAS...92.9977B](https://ui.adsabs.harvard.edu/abs/1995PNAS...92.9977B). [doi](/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.1073/pnas.92.22.9977](https://doi.org/10.1073%2Fpnas.92.22.9977). [PMC](/wiki/PMC_\(identifier\) "PMC \(identifier\)") [40721](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC40721). [PMID](/wiki/PMID_\(identifier\) "PMID \(identifier\)") [7479812](https://pubmed.ncbi.nlm.nih.gov/7479812).
  * Steven Bird, Ewan Klein, and Edward Loper (2009). _Natural Language Processing with Python_. O'Reilly Media. [ISBN](/wiki/ISBN_\(identifier\) "ISBN \(identifier\)") [978-0-596-51649-9](/wiki/Special:BookSources/978-0-596-51649-9 "Special:BookSources/978-0-596-51649-9").
  * [Kenna Hughes-Castleberry](/w/index.php?title=Kenna_Hughes-Castleberry&action=edit&redlink=1 "Kenna Hughes-Castleberry \(page does not exist\)"), "A Murder Mystery Puzzle: The literary puzzle _[Cain's Jawbone](/wiki/Cain%27s_Jawbone "Cain's Jawbone")_ , which has stumped humans for decades, reveals the limitations of natural-language-processing algorithms", _[Scientific American](/wiki/Scientific_American "Scientific American")_ , vol. 329, no. 4 (November 2023), pp. 81–82. "This murder mystery competition has revealed that although NLP ([natural-language processing](/wiki/Natural-language_processing "Natural-language processing")) models are capable of incredible feats, their abilities are very much limited by the amount of [context](/wiki/Context_\(linguistics\) "Context \(linguistics\)") they receive. This [...] could cause [difficulties] for researchers who hope to use them to do things such as analyze [ancient languages](/wiki/Ancient_language "Ancient language"). In some cases, there are few historical records on long-gone [civilizations](/wiki/Civilization "Civilization") to serve as [training data](/wiki/Training_data "Training data") for such a purpose." (p. 82.)
  * Daniel Jurafsky and James H. Martin (2008). _Speech and Language Processing_ , 2nd edition. Pearson Prentice Hall. [ISBN](/wiki/ISBN_\(identifier\) "ISBN \(identifier\)") [978-0-13-187321-6](/wiki/Special:BookSources/978-0-13-187321-6 "Special:BookSources/978-0-13-187321-6").
  * Mohamed Zakaria Kurdi (2016). _Natural Language Processing and Computational Linguistics: speech, morphology, and syntax_ , Volume 1. ISTE-Wiley. [ISBN](/wiki/ISBN_\(identifier\) "ISBN \(identifier\)") [978-1848218482](/wiki/Special:BookSources/978-1848218482 "Special:BookSources/978-1848218482").
  * Mohamed Zakaria Kurdi (2017). _Natural Language Processing and Computational Linguistics: semantics, discourse, and applications_ , Volume 2. ISTE-Wiley. [ISBN](/wiki/ISBN_\(identifier\) "ISBN \(identifier\)") [978-1848219212](/wiki/Special:BookSources/978-1848219212 "Special:BookSources/978-1848219212").
  * Christopher D. Manning, Prabhakar Raghavan, and Hinrich Schütze (2008). _Introduction to Information Retrieval_. Cambridge University Press. [ISBN](/wiki/ISBN_\(identifier\) "ISBN \(identifier\)") [978-0-521-86571-5](/wiki/Special:BookSources/978-0-521-86571-5 "Special:BookSources/978-0-521-86571-5"). [Official html and pdf versions available without charge.](http://nlp.stanford.edu/IR-book/)
  * Christopher D. Manning and Hinrich Schütze (1999). _Foundations of Statistical Natural Language Processing_. The MIT Press. [ISBN](/wiki/ISBN_\(identifier\) "ISBN \(identifier\)") [978-0-262-13360-9](/wiki/Special:BookSources/978-0-262-13360-9 "Special:BookSources/978-0-262-13360-9").
  * David M. W. Powers and Christopher C. R. Turk (1989). _Machine Learning of Natural Language_. Springer-Verlag. [ISBN](/wiki/ISBN_\(identifier\) "ISBN \(identifier\)") [978-0-387-19557-5](/wiki/Special:BookSources/978-0-387-19557-5 "Special:BookSources/978-0-387-19557-5").

## External links

[[edit](/w/index.php?title=Natural_language_processing&action=edit&section=20 "Edit section: External links")]

  * [![](//upload.wikimedia.org/wikipedia/en/thumb/4/4a/Commons-logo.svg/20px-Commons-logo.svg.png)](/wiki/File:Commons-logo.svg) Media related to [Natural language processing](https://commons.wikimedia.org/wiki/Category:Natural_language_processing "commons:Category:Natural language processing") at Wikimedia Commons

  * [v](/wiki/Template:Natural_language_processing "Template:Natural language processing")
  * [t](/wiki/Template_talk:Natural_language_processing "Template talk:Natural language processing")
  * [e](/wiki/Special:EditPage/Template:Natural_language_processing "Special:EditPage/Template:Natural language processing")

Natural language processing  
---  
General terms| 

  * [AI-complete](/wiki/AI-complete "AI-complete")
  * [Bag-of-words](/wiki/Bag-of-words_model "Bag-of-words model")
  * [_n_ -gram](/wiki/N-gram "N-gram")
    * [Bigram](/wiki/Bigram "Bigram")
    * [Trigram](/wiki/Trigram "Trigram")
  * [Computational linguistics](/wiki/Computational_linguistics "Computational linguistics")
  * [Natural language understanding](/wiki/Natural_language_understanding "Natural language understanding")
  * [Stop words](/wiki/Stop_word "Stop word")
  * [Text processing](/wiki/Text_processing "Text processing")

  
[Text analysis](/wiki/Text_mining "Text mining")| 

  * [Argument mining](/wiki/Argument_mining "Argument mining")
  * [Collocation extraction](/wiki/Collocation_extraction "Collocation extraction")
  * [Concept mining](/wiki/Concept_mining "Concept mining")
  * [Coreference resolution](/wiki/Coreference#Coreference_resolution "Coreference")
  * [Deep linguistic processing](/wiki/Deep_linguistic_processing "Deep linguistic processing")
  * [Distant reading](/wiki/Distant_reading "Distant reading")
  * [Information extraction](/wiki/Information_extraction "Information extraction")
  * [Named-entity recognition](/wiki/Named-entity_recognition "Named-entity recognition")
  * [Ontology learning](/wiki/Ontology_learning "Ontology learning")
  * [Parsing](/wiki/Parsing "Parsing")
    * [semantic](/wiki/Semantic_parsing "Semantic parsing")
    * [syntactic](/wiki/Syntactic_parsing_\(computational_linguistics\) "Syntactic parsing \(computational linguistics\)")
  * [Part-of-speech tagging](/wiki/Part-of-speech_tagging "Part-of-speech tagging")
  * [Semantic analysis](/wiki/Semantic_analysis_\(machine_learning\) "Semantic analysis \(machine learning\)")
  * [Semantic role labeling](/wiki/Semantic_role_labeling "Semantic role labeling")
  * [Semantic decomposition](/wiki/Semantic_decomposition_\(natural_language_processing\) "Semantic decomposition \(natural language processing\)")
  * [Semantic similarity](/wiki/Semantic_similarity "Semantic similarity")
  * [Sentiment analysis](/wiki/Sentiment_analysis "Sentiment analysis")

  * [Terminology extraction](/wiki/Terminology_extraction "Terminology extraction")
  * [Text mining](/wiki/Text_mining "Text mining")
  * [Textual entailment](/wiki/Textual_entailment "Textual entailment")
  * [Truecasing](/wiki/Truecasing "Truecasing")
  * [Word-sense disambiguation](/wiki/Word-sense_disambiguation "Word-sense disambiguation")
  * [Word-sense induction](/wiki/Word-sense_induction "Word-sense induction")

| [Text segmentation](/wiki/Text_segmentation "Text segmentation")| 

  * [Compound-term processing](/wiki/Compound-term_processing "Compound-term processing")
  * [Lemmatisation](/wiki/Lemmatisation "Lemmatisation")
  * [Lexical analysis](/wiki/Lexical_analysis "Lexical analysis")
  * [Text chunking](/wiki/Shallow_parsing "Shallow parsing")
  * [Stemming](/wiki/Stemming "Stemming")
  * [Sentence segmentation](/wiki/Sentence_boundary_disambiguation "Sentence boundary disambiguation")
  * [Word segmentation](/wiki/Word#Word_boundaries "Word")

  
---|---  
  
[Automatic summarization](/wiki/Automatic_summarization "Automatic summarization")| 

  * [Multi-document summarization](/wiki/Multi-document_summarization "Multi-document summarization")
  * [Sentence extraction](/wiki/Sentence_extraction "Sentence extraction")
  * [Text simplification](/wiki/Text_simplification "Text simplification")

  
[Machine translation](/wiki/Machine_translation "Machine translation")| 

  * [Computer-assisted](/wiki/Computer-assisted_translation "Computer-assisted translation")
  * [Example-based](/wiki/Example-based_machine_translation "Example-based machine translation")
  * [Rule-based](/wiki/Rule-based_machine_translation "Rule-based machine translation")
  * [Statistical](/wiki/Statistical_machine_translation "Statistical machine translation")
  * [Transfer-based](/wiki/Transfer-based_machine_translation "Transfer-based machine translation")
  * [Neural](/wiki/Neural_machine_translation "Neural machine translation")

  
[Distributional semantics](/wiki/Distributional_semantics "Distributional semantics") models| 

  * [BERT](/wiki/BERT_\(language_model\) "BERT \(language model\)")
  * [Document-term matrix](/wiki/Document-term_matrix "Document-term matrix")
  * [Explicit semantic analysis](/wiki/Explicit_semantic_analysis "Explicit semantic analysis")
  * [fastText](/wiki/FastText "FastText")
  * [GloVe](/wiki/GloVe "GloVe")
  * [Language model](/wiki/Language_model "Language model")
    * [large](/wiki/Large_language_model "Large language model")
    * [small](/wiki/Small_language_model "Small language model")
  * [Latent semantic analysis](/wiki/Latent_semantic_analysis "Latent semantic analysis")
  * [Long short-term memory](/wiki/Long_short-term_memory "Long short-term memory")
  * [Seq2seq](/wiki/Seq2seq "Seq2seq")
  * [Transformer](/wiki/Transformer_\(deep_learning_architecture\) "Transformer \(deep learning architecture\)")
  * [Word embedding](/wiki/Word_embedding "Word embedding")
  * [Word2vec](/wiki/Word2vec "Word2vec")

  
[Language resources](/wiki/Language_resource "Language resource"),  
datasets and corpora| | Types and  
standards| 

  * [Corpus linguistics](/wiki/Corpus_linguistics "Corpus linguistics")
  * [Lexical resource](/wiki/Lexical_resource "Lexical resource")
  * [Linguistic Linked Open Data](/wiki/Linguistic_Linked_Open_Data "Linguistic Linked Open Data")
  * [Machine-readable dictionary](/wiki/Machine-readable_dictionary "Machine-readable dictionary")
  * [Parallel text](/wiki/Parallel_text "Parallel text")
  * [PropBank](/wiki/PropBank "PropBank")
  * [Semantic network](/wiki/Semantic_network "Semantic network")
  * [Simple Knowledge Organization System](/wiki/Simple_Knowledge_Organization_System "Simple Knowledge Organization System")
  * [Speech corpus](/wiki/Speech_corpus "Speech corpus")
  * [Text corpus](/wiki/Text_corpus "Text corpus")
  * [Thesaurus (information retrieval)](/wiki/Thesaurus_\(information_retrieval\) "Thesaurus \(information retrieval\)")
  * [Treebank](/wiki/Treebank "Treebank")
  * [Universal Dependencies](/wiki/Universal_Dependencies "Universal Dependencies")

  
---|---  
Data| 

  * [BabelNet](/wiki/BabelNet "BabelNet")
  * [Bank of English](/wiki/Bank_of_English "Bank of English")
  * [DBpedia](/wiki/DBpedia "DBpedia")
  * [FrameNet](/wiki/FrameNet "FrameNet")
  * [Google Ngram Viewer](/wiki/Google_Ngram_Viewer "Google Ngram Viewer")
  * [UBY](/wiki/UBY "UBY")
  * [WordNet](/wiki/WordNet "WordNet")
  * [Wikidata](/wiki/Wikidata "Wikidata")

  
  
[Automatic identification  
and data capture](/wiki/Automatic_identification_and_data_capture "Automatic identification and data capture")| 

  * [Speech recognition](/wiki/Speech_recognition "Speech recognition")
  * [Speech segmentation](/wiki/Speech_segmentation "Speech segmentation")
  * [Speech synthesis](/wiki/Speech_synthesis "Speech synthesis")
  * [Natural language generation](/wiki/Natural_language_generation "Natural language generation")
  * [Optical character recognition](/wiki/Optical_character_recognition "Optical character recognition")

  
[Topic model](/wiki/Topic_model "Topic model")| 

  * [Document classification](/wiki/Document_classification "Document classification")
  * [Latent Dirichlet allocation](/wiki/Latent_Dirichlet_allocation "Latent Dirichlet allocation")
  * [Pachinko allocation](/wiki/Pachinko_allocation "Pachinko allocation")

  
[Computer-assisted  
reviewing](/wiki/Computer-assisted_reviewing "Computer-assisted reviewing")| 

  * [Automated essay scoring](/wiki/Automated_essay_scoring "Automated essay scoring")
  * [Concordancer](/wiki/Concordancer "Concordancer")
  * [Grammar checker](/wiki/Grammar_checker "Grammar checker")
  * [Predictive text](/wiki/Predictive_text "Predictive text")
  * [Pronunciation assessment](/wiki/Pronunciation_assessment "Pronunciation assessment")
  * [Spell checker](/wiki/Spell_checker "Spell checker")

  
[Natural language  
user interface](/wiki/Natural-language_user_interface "Natural-language user interface")| 

  * [Chatbot](/wiki/Chatbot "Chatbot")
  * [Interactive fiction](/wiki/Interactive_fiction "Interactive fiction")
  * [Question answering](/wiki/Question_answering "Question answering")
  * [Virtual assistant](/wiki/Virtual_assistant "Virtual assistant")
  * [Voice user interface](/wiki/Voice_user_interface "Voice user interface")

  
Related| 

  * [Formal semantics](/wiki/Formal_semantics_\(natural_language\) "Formal semantics \(natural language\)")
  * [Hallucination](/wiki/Hallucination_\(artificial_intelligence\) "Hallucination \(artificial intelligence\)")
  * [Natural Language Toolkit](/wiki/Natural_Language_Toolkit "Natural Language Toolkit")
  * [spaCy](/wiki/SpaCy "SpaCy")

  
  
[Portal](/wiki/Wikipedia:Contents/Portals "Wikipedia:Contents/Portals"):

  * [![icon](//upload.wikimedia.org/wikipedia/commons/thumb/d/de/Globe_of_letters.svg/20px-Globe_of_letters.svg.png)](/wiki/File:Globe_of_letters.svg) [Language](/wiki/Portal:Language "Portal:Language")

[Authority control databases](/wiki/Help:Authority_control "Help:Authority control") [![Edit this at Wikidata](//upload.wikimedia.org/wikipedia/en/thumb/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg/20px-OOjs_UI_icon_edit-ltr-progressive.svg.png)](https://www.wikidata.org/wiki/Q30642#identifiers "Edit this at Wikidata")  
---  
National| 

  * [United States](https://id.loc.gov/authorities/sh88002425)
  * [Japan](https://id.ndl.go.jp/auth/ndlna/00562347)
  * [Czech Republic](https://aleph.nkp.cz/F/?func=find-c&local_base=aut&ccl_term=ica=ph427562&CON_LNG=ENG)
  * [Israel](https://www.nli.org.il/en/authorities/987007536703305171)

  
Other| 

  * [Yale LUX](https://lux.collections.yale.edu/view/concept/e0fc4a1c-7602-43f9-9cea-0d8bb49039b8)

  
  
![](https://en.wikipedia.org/wiki/Special:CentralAutoLogin/start?useformat=desktop&type=1x1&usesul3=1)

Retrieved from "[https://en.wikipedia.org/w/index.php?title=Natural_language_processing&oldid=1321938724](https://en.wikipedia.org/w/index.php?title=Natural_language_processing&oldid=1321938724)"

[Categories](/wiki/Help:Category "Help:Category"): 

  * [Natural language processing](/wiki/Category:Natural_language_processing "Category:Natural language processing")
  * [Computational fields of study](/wiki/Category:Computational_fields_of_study "Category:Computational fields of study")
  * [Computational linguistics](/wiki/Category:Computational_linguistics "Category:Computational linguistics")
  * [Speech recognition](/wiki/Category:Speech_recognition "Category:Speech recognition")

Hidden categories: 

  * [All accuracy disputes](/wiki/Category:All_accuracy_disputes "Category:All accuracy disputes")
  * [Accuracy disputes from December 2013](/wiki/Category:Accuracy_disputes_from_December_2013 "Category:Accuracy disputes from December 2013")
  * [Harv and Sfn no-target errors](/wiki/Category:Harv_and_Sfn_no-target_errors "Category:Harv and Sfn no-target errors")
  * [CS1 errors: periodical ignored](/wiki/Category:CS1_errors:_periodical_ignored "Category:CS1 errors: periodical ignored")
  * [CS1 maint: location](/wiki/Category:CS1_maint:_location "Category:CS1 maint: location")
  * [Articles with short description](/wiki/Category:Articles_with_short_description "Category:Articles with short description")
  * [Short description is different from Wikidata](/wiki/Category:Short_description_is_different_from_Wikidata "Category:Short description is different from Wikidata")
  * [Articles needing additional references from May 2024](/wiki/Category:Articles_needing_additional_references_from_May_2024 "Category:Articles needing additional references from May 2024")
  * [All articles needing additional references](/wiki/Category:All_articles_needing_additional_references "Category:All articles needing additional references")
  * [Wikipedia articles needing rewrite from July 2025](/wiki/Category:Wikipedia_articles_needing_rewrite_from_July_2025 "Category:Wikipedia articles needing rewrite from July 2025")
  * [All articles needing rewrite](/wiki/Category:All_articles_needing_rewrite "Category:All articles needing rewrite")
  * [Wikipedia articles needing reorganization from July 2025](/wiki/Category:Wikipedia_articles_needing_reorganization_from_July_2025 "Category:Wikipedia articles needing reorganization from July 2025")
  * [Articles with multiple maintenance issues](/wiki/Category:Articles_with_multiple_maintenance_issues "Category:Articles with multiple maintenance issues")
  * [All articles with unsourced statements](/wiki/Category:All_articles_with_unsourced_statements "Category:All articles with unsourced statements")
  * [Articles with unsourced statements from May 2024](/wiki/Category:Articles_with_unsourced_statements_from_May_2024 "Category:Articles with unsourced statements from May 2024")
  * [Webarchive template wayback links](/wiki/Category:Webarchive_template_wayback_links "Category:Webarchive template wayback links")
  * [Commons category link from Wikidata](/wiki/Category:Commons_category_link_from_Wikidata "Category:Commons category link from Wikidata")

  * This page was last edited on 13 November 2025, at 14:08 (UTC).

  * [About Wikipedia](/wiki/Wikipedia:About)
  * [Disclaimers](/wiki/Wikipedia:General_disclaimer)
  * [Contact Wikipedia](//en.wikipedia.org/wiki/Wikipedia:Contact_us)
  * [Code of Conduct](https://foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:Universal_Code_of_Conduct)
  * [Developers](https://developer.wikimedia.org)
  * [Statistics](https://stats.wikimedia.org/#/en.wikipedia.org)
  * [Mobile view](//en.wikipedia.org/w/index.php?title=Natural_language_processing&mobileaction=toggle_view_mobile)

  * [![Wikimedia Foundation](/static/images/footer/wikimedia.svg)](https://www.wikimedia.org/)
  * [![Powered by MediaWiki](/w/resources/assets/mediawiki_compact.svg)](https://www.mediawiki.org/)

Search

Search

Toggle the table of contents

Natural language processing

[ ](#) [ ](#) [ ](#) [ ](#) [ ](#) [ ](#) [ ](#) [ ](#)

71 languages [ Add topic ](#)

  *[v]: View this template
  *[t]: Discuss this template
  *[e]: Edit this template