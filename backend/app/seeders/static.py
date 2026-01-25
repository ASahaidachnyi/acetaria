from sqlalchemy import text

from app.core.db import get_session


def seed_static():
    """
    Seed static data intended to be prepared before the application starts,
    like chars, lightcones, game modes, etc.
    """

    session = next(get_session())
    session.exec(text(DATA))  # type: ignore
    print("DONE")


DATA = """
INSERT INTO public."char" (id,"name","icon_url",rarity) VALUES
	 ('1002','Dan Heng','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1002.png',4),
	 ('1107','Clara','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1107.png',5),
	 ('1001','March 7th • Preservation','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1001.png',4),
	 ('1108','Sampo','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1108.png',4),
	 ('1415','Cyrene','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1415.png',5),
	 ('1321','The Dahlia','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1321.png',5),
	 ('1109','Hook','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1109.png',4),
	 ('1110','Lynx','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1110.png',4),
	 ('1111','Luka','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1111.png',4),
	 ('1112','Topaz & Numby','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1112.png',5),
	 ('1004','Welt','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1004.png',5),
	 ('1009','Asta','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1009.png',4),
	 ('1104','Gepard','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1104.png',5),
	 ('1008','Arlan','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1008.png',4),
	 ('1201','Qingque','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1201.png',4),
	 ('1014','Saber','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1014.png',5),
	 ('1005','Kafka','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1005.png',5),
	 ('1015','Archer','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1015.png',5),
	 ('1006','Silver Wolf','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1006.png',5),
	 ('1013','Herta','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1013.png',4),
	 ('1003','Himeko','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1003.png',5),
	 ('1202','Tingyun','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1202.png',4),
	 ('1105','Natasha','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1105.png',4),
	 ('1106','Pela','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1106.png',4),
	 ('1103','Serval','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1103.png',4),
	 ('1101','Bronya','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1101.png',5),
	 ('1306','Sparkle','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1306.png',5),
	 ('1204','Jing Yuan','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1204.png',5),
	 ('1305','Dr. Ratio','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1305.png',5),
	 ('1220','Feixiao','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1220.png',5),
	 ('1307','Black Swan','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1307.png',5),
	 ('1205','Blade','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1205.png',5),
	 ('1310','Firefly','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1310.png',5),
	 ('1210','Guinaifen','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1210.png',4),
	 ('1225','Fugue','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1225.png',5),
	 ('1215','Hanya','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1215.png',4),
	 ('1221','Yunli','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1221.png',5),
	 ('1308','Acheron','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1308.png',5),
	 ('1313','Sunday','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1313.png',5),
	 ('1212','Jingliu','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1212.png',5),
	 ('1102','Seele','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1102.png',5),
	 ('1208','Fu Xuan','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1208.png',5),
	 ('1223','Moze','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1223.png',4),
	 ('1203','Luocha','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1203.png',5),
	 ('1209','Yanqing','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1209.png',5),
	 ('1207','Yukong','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1207.png',4),
	 ('1206','Sushang','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1206.png',4),
	 ('1214','Xueyi','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1214.png',4),
	 ('1222','Lingsha','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1222.png',5),
	 ('1224','March 7th • The Hunt','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1224.png',4),
	 ('1211','Bailu','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1211.png',5),
	 ('1403','Tribbie','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1403.png',5),
	 ('1412','Cerydra','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1412.png',5),
	 ('1303','Ruan Mei','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1303.png',5),
	 ('1217','Huohuo','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1217.png',5),
	 ('1314','Jade','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1314.png',5),
	 ('1317','Rappa','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1317.png',5),
	 ('1410','Hysilens','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1410.png',5),
	 ('1404','Mydei','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1404.png',5),
	 ('1218','Jiaoqiu','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1218.png',5),
	 ('1402','Aglaea','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1402.png',5),
	 ('1302','Argenti','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1302.png',5),
	 ('1312','Misha','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1312.png',4),
	 ('1304','Aventurine','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1304.png',5),
	 ('1401','The Herta','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1401.png',5),
	 ('1405','Anaxa','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1405.png',5),
	 ('1301','Gallagher','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1301.png',4),
	 ('1315','Boothill','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1315.png',5),
	 ('1309','Robin','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1309.png',5),
	 ('1414','Dan Heng • Permansor Terrae','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1414.png',5),
	 ('8008','Remembrance MC','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/8008.png',5),
	 ('8006','Harmony MC','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/8006.png',5),
	 ('8004','Preservation MC','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/8004.png',5),
	 ('1406','Cipher','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1406.png',5),
	 ('8002','Destruction MC','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/8002.png',5),
	 ('1409','Hyacine','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1409.png',5),
	 ('1408','Phainon','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1408.png',5),
	 ('1413','Evernight','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1413.png',5),
	 ('1407','Castorice','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1407.png',5),
	 ('1213','Dan Heng • Imbibitor Lunae','https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/icon/character/1213.png',5);

;

INSERT INTO public.lightcone (id,"name",sig_of_char_id,rarity,icon_url) VALUES
	 (23051,'Though Worlds Apart',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23051.png'),
	 (23049,'To Evernight''s Stars',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23049.png'),
	 (23050,'Never Forget Her Flame',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23050.png'),
	 (21000,'Post-Op Conversation',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21000.png'),
	 (21003,'Only Silence Remains',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21003.png'),
	 (21060,'A Dream Scented in Wheat',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21060.png'),
	 (21007,'Shared Feeling',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21007.png'),
	 (21009,'Landau''s Choice',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21009.png'),
	 (21045,'After the Charmony Fall',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21045.png'),
	 (21010,'Swordplay',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21010.png'),
	 (23024,'Along the Passing Shore',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23024.png'),
	 (21011,'Planetary Rendezvous',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21011.png'),
	 (21012,'A Secret Vow',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21012.png'),
	 (23030,'Dance at Sunset',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23030.png'),
	 (23052,'This Love, Forever',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23052.png'),
	 (23029,'Those Many Springs',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23029.png'),
	 (21008,'Eyes of the Prey',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21008.png'),
	 (21018,'Dance! Dance! Dance!',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21018.png'),
	 (21001,'Good Night and Sleep Well',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21001.png'),
	 (21002,'Day One of My New Life',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21002.png'),
	 (21004,'Memories of the Past',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21004.png'),
	 (21005,'The Moles Welcome You',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21005.png'),
	 (21006,'The Birth of the Self',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21006.png'),
	 (21013,'Make the World Clamor',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21013.png'),
	 (21014,'Perfect Timing',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21014.png'),
	 (21015,'Resolution Shines As Pearls of Sweat',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21015.png'),
	 (21016,'Trend of the Universal Market',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21016.png'),
	 (21017,'Subscribe for More!',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21017.png'),
	 (21019,'Under the Blue Sky',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21019.png'),
	 (21020,'Geniuses'' Repose',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21020.png'),
	 (21021,'Quid Pro Quo',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21021.png'),
	 (21022,'Fermata',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21022.png'),
	 (21023,'We Are Wildfire',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21023.png'),
	 (21024,'River Flows in Spring',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21024.png'),
	 (21025,'Past and Future',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21025.png'),
	 (21026,'Woof! Walk Time!',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21026.png'),
	 (21027,'The Seriousness of Breakfast',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21027.png'),
	 (21028,'Warmth Shortens Cold Nights',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21028.png'),
	 (21029,'We Will Meet Again',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21029.png'),
	 (21030,'This Is Me!',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21030.png'),
	 (21035,'What Is Real?',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21035.png'),
	 (21036,'Dreamville Adventure',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21036.png'),
	 (21037,'Final Victor',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21037.png'),
	 (21038,'Flames Afar',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21038.png'),
	 (21039,'Destiny''s Threads Forewoven',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21039.png'),
	 (21040,'The Day The Cosmos Fell',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21040.png'),
	 (21041,'It''s Showtime',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21041.png'),
	 (21042,'Indelible Promise',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21042.png'),
	 (21043,'Concert for Two',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21043.png'),
	 (21044,'Boundless Choreo',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21044.png'),
	 (21046,'Poised to Bloom',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21046.png'),
	 (21047,'Shadowed by Night',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21047.png'),
	 (21048,'Dream''s Montage',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21048.png'),
	 (21050,'Victory In a Blink',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21050.png'),
	 (21051,'Geniuses'' Greetings',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21051.png'),
	 (21032,'Carve the Moon, Weave the Clouds',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21032.png'),
	 (21033,'Nowhere to Run',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21033.png'),
	 (21031,'Return to Darkness',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21031.png'),
	 (21052,'Sweat Now, Cry Less',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21052.png'),
	 (21034,'Today Is Another Peaceful Day',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21034.png'),
	 (22001,'Hey, Over Here',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/22001.png'),
	 (22002,'For Tomorrow''s Journey',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/22002.png'),
	 (22003,'Ninja Record: Sound Hunt',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/22003.png'),
	 (22004,'The Great Cosmic Enterprise',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/22004.png'),
	 (22005,'The Forever Victual',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/22005.png'),
	 (22000,'Before the Tutorial Mission Starts',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/22000.png'),
	 (23003,'But the Battle Isn''t Over',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23003.png'),
	 (23008,'Echoes of the Coffin',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23008.png'),
	 (21058,'A Trail of Bygone Blood',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21058.png'),
	 (21056,'In Pursuit of the Wind',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21056.png'),
	 (23004,'In the Name of the World',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23004.png'),
	 (23001,'In the Night',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23001.png'),
	 (23007,'Incessant Rain',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23007.png'),
	 (23005,'Moment of Victory',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23005.png'),
	 (23000,'Night on the Milky Way',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23000.png'),
	 (23006,'Patience Is All You Need',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23006.png'),
	 (21057,'The Flower Remembers',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21057.png'),
	 (23002,'Something Irreplaceable',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23002.png'),
	 (21055,'Unto Tomorrow''s Morrow',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21055.png'),
	 (21054,'The Story''s Next Page',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21054.png'),
	 (21053,'Journey, Forever Peaceful',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21053.png'),
	 (21062,'See You at the End',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21062.png'),
	 (21061,'Holiday Thermae Escapade',NULL,4,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/21061.png'),
	 (23015,'Brighter Than the Sun',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23015.png'),
	 (23020,'Baptism of Pure Thought',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23020.png'),
	 (23010,'Before Dawn',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23010.png'),
	 (23021,'Earthly Escapade',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23021.png'),
	 (23031,'I Venture Forth to Hunt',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23031.png'),
	 (23026,'Flowing Nightglow',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23026.png'),
	 (23014,'I Shall Be My Own Sword',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23014.png'),
	 (23023,'Inherently Unjust Destiny',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23023.png'),
	 (23039,'Flame of Blood, Blaze My Path',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23039.png'),
	 (23017,'Night of Fright',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23017.png'),
	 (23033,'Ninjutsu Inscription: Dazzling Evilbreaker',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23033.png'),
	 (23019,'Past Self in Mirror',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23019.png'),
	 (23022,'Reforged Remembrance',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23022.png'),
	 (23027,'Sailing Towards a Second Life',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23027.png'),
	 (23032,'Scent Alone Stays True',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23032.png'),
	 (23011,'She Already Shut Her Eyes',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23011.png'),
	 (23012,'Sleep Like the Dead',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23012.png'),
	 (23028,'Yet Hope Is Priceless',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23028.png'),
	 (23016,'Worrisome, Blissful',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23016.png'),
	 (23025,'Whereabouts Should Dreams Rest',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23025.png'),
	 (23013,'Time Waits for No One',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23013.png'),
	 (23009,'The Unreachable Side',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23009.png'),
	 (23018,'An Instant Before A Gaze',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23018.png'),
	 (23045,'A Thankless Coronation',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23045.png'),
	 (23048,'Epoch Etched in Golden Blood',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23048.png'),
	 (23040,'Make Farewells More Beautiful',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23040.png'),
	 (23044,'Thus Burns the Dawn',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23044.png'),
	 (23043,'Lies Dance on the Breeze',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23043.png'),
	 (23041,'Life Should Be Cast to Flames',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23041.png'),
	 (23038,'If Time Were a Flower',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23038.png'),
	 (23046,'The Hell Where Ideals Burn',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23046.png'),
	 (23037,'Into the Unreachable Veil',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23037.png'),
	 (23035,'Long Road Leads Home',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23035.png'),
	 (24000,'On the Fall of an Aeon',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/24000.png'),
	 (24001,'Cruising in the Stellar Sea',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/24001.png'),
	 (24002,'Texture of Memories',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/24002.png'),
	 (24003,'Solitary Healing',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/24003.png'),
	 (23042,'Long May Rainbows Adorn the Sky',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23042.png'),
	 (23047,'Why Does the Ocean Sing',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23047.png'),
	 (23036,'Time Woven Into Gold',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23036.png'),
	 (23034,'A Grounded Ascent',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/23034.png'),
	 (24004,'Eternal Calculus',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/24004.png'),
	 (24005,'Memory''s Curtain Never Falls',NULL,5,'https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/image/light_cone_portrait/24005.png');


--charId, sigId
--[
--    "(1001, 21002),",
--    "(1002, 24001),",
--    "(1003, 23000),",
--    "(1004, 23004),",
--    "(1005, 23006),",
--    "(1006, 23007),",
--    "(1008, 21012),",
--    "(1009, 21032),",
--    "(1013, 23000),",
--    "(1101, 23003),",
--    "(1102, 23001),",
--    "(1103, 21013),",
--    "(1104, 23005),",
--    "(1105, 21000),",
--    "(1106, 21015),",
--    "(1107, 23002),",
--    "(1108, 21008),",
--    "(1109, 21005),",
--    "(1110, 21028),",
--    "(1111, 21015),",
--    "(1112, 23016),",
--    "(1201, 21034),",
--    "(1202, 21032),",
--    "(1203, 23008),",
--    "(1204, 23010),",
--    "(1205, 23009),",
--    "(1206, 21010),",
--    "(1207, 21025),",
--    "(1208, 23011),",
--    "(1209, 23012),",
--    "(1210, 21008),",
--    "(1211, 23013),",
--    "(1212, 23014),",
--    "(1213, 23015),",
--    "(1214, 21042),",
--    "(1215, 21011),",
--    "(1217, 23017),",
--    "(1218, 23029),",
--    "(1220, 23031),",
--    "(1221, 23030),",
--    "(1222, 23032),",
--    "(1223, 21010),",
--    "(1224, 23012),",
--    "(1225, 23035),",
--    "(1301, 21035),",
--    "(1302, 23018),",
--    "(1303, 23019),",
--    "(1304, 23023),",
--    "(1305, 23020),",
--    "(1306, 23021),",
--    "(1307, 23022),",
--    "(1308, 23024),",
--    "(1309, 23026),",
--    "(1310, 23025),",
--    "(1312, 24000),",
--    "(1313, 23034),",
--    "(1314, 23028),",
--    "(1315, 23027),",
--    "(1317, 23033),",
--    "(1401, 23037),",
--    "(1402, 23036),",
--    "(1403, 23038),",
--    "(1404, 23039),",
--    "(1405, 23041),",
--    "(1406, 23043),",
--    "(1407, 23040),",
--    "(1408, 23044),",
--    "(1409, 23042),",
--    "(1410, 23047),",
--    "(1412, 23048),",
--    "(8001, 23015),",
--    "(8002, 23015),",
--    "(8003, 23005),",
--    "(8004, 23005),",
--    "(8005, 21056),",
--    "(8006, 21056),",
--    "(8007, 21050),",
--    "(8008, 21050),",
--    "(1413, 23049),",
--    "(1414, 23051),",
--    "(1415, 23052),",
--    "(1321, 23050),"
--]

INSERT INTO public."cost" ("name") values ('default manual');

INSERT INTO public."cost" ("name") values ('Limited 5 stars');

INSERT INTO public."cost" ("name") values ('Standard 5 stars');
;
--select * from public.game_mode gm
;
insert into public.game_mode (kind, primary_score_kind, primary_score_reverse_sorting ,secondary_score_kind, secondary_score_reverse_sorting, "name" ) values
('Moc12'::gamemodekindenum, 'Cycles'::resultkindenum, false, null, null, 'MoC 12'),
('Pf'::gamemodekindenum, 'Score'::resultkindenum, true , 'Cycles'::resultkindenum, false, 'PF'),
('As'::gamemodekindenum, 'Score'::resultkindenum, true, null, null, 'AS'),
('Aak1'::gamemodekindenum, 'Cycles'::resultkindenum, false, null, null, 'AA Knight 1'),
('Aak2'::gamemodekindenum, 'Cycles'::resultkindenum, false, null, null, 'AA Knight 2'),
('Aak3'::gamemodekindenum, 'Cycles'::resultkindenum, false, null, null, 'AA Knight 3'),
('Aacm'::gamemodekindenum, 'Cycles'::resultkindenum, false, null, null, 'AA lv100'),
('Aazz'::gamemodekindenum, 'Av'::resultkindenum, false, null, null, 'AA lv120 Plight');
;
;
create type gme_tuple as (
	"from" timestamp,
	"to" timestamp,
	"name" varchar,
	"stage_id" int4
)
;
insert into public.game_mode_entry ("name", active_from, active_to , game_mode_id , stage_id )
select --,,,,
ds."name", ds."from", ds."to", gm.id, ds."stage_id"
from unnest(ARRAY[
(('2026-01-19 00:00:00'::date)::timestamp, ('2026-03-02 00:00:00'::date)::timestamp, 'MoC 3.8 Dark Sam'::varchar, 30119121::int4)::gme_tuple,
(('2026-01-19 00:00:00'::date)::timestamp, ('2026-03-02 00:00:00'::date)::timestamp, 'MoC 3.8 Cocolia'::varchar, 30119122::int4)::gme_tuple,--
(('2025-12-08 00:00:00'::date)::timestamp, ('2026-01-19 00:00:00'::date)::timestamp, 'MoC 3.7 Sam'::varchar, 30118121::int4)::gme_tuple,
(('2025-12-08 00:00:00'::date)::timestamp, ('2026-01-19 00:00:00'::date)::timestamp, 'MoC 3.7 Hoolay'::varchar, 30118122::int4)::gme_tuple,--
(('2025-10-27 00:00:00'::date)::timestamp, ('2025-12-08 00:00:00'::date)::timestamp, 'MoC 3.6 Reaver'::varchar, 30117121::int4)::gme_tuple,
(('2025-10-27 00:00:00'::date)::timestamp, ('2025-12-08 00:00:00'::date)::timestamp, 'MoC 3.6 Ichor'::varchar, 30117122::int4)::gme_tuple,--
(('2025-09-15 00:00:00'::date)::timestamp, ('2025-10-27 00:00:00'::date)::timestamp, 'MoC 3.5 Gepard'::varchar, 30116121::int4)::gme_tuple,
(('2025-09-15 00:00:00'::date)::timestamp, ('2025-10-27 00:00:00'::date)::timestamp, 'MoC 3.5 Zandar'::varchar, 30116122::int4)::gme_tuple,--
(('2025-08-04 00:00:00'::date)::timestamp, ('2025-09-15 00:00:00'::date)::timestamp, 'MoC 3.4 Svarog'::varchar, 30115121::int4)::gme_tuple,
(('2025-08-04 00:00:00'::date)::timestamp, ('2025-09-15 00:00:00'::date)::timestamp, 'MoC 3.4 Aventurine'::varchar, 30115122::int4)::gme_tuple,--
(('2025-06-23 00:00:00'::date)::timestamp, ('2025-08-04 00:00:00'::date)::timestamp, 'MoC 3.3 True Sting'::varchar, 30114121::int4)::gme_tuple,
(('2025-06-23 00:00:00'::date)::timestamp, ('2025-08-04 00:00:00'::date)::timestamp, 'MoC 3.3 Hoolay'::varchar, 30114122::int4)::gme_tuple,--
(('2025-05-12 00:00:00'::date)::timestamp, ('2025-06-23 00:00:00'::date)::timestamp, 'MoC 3.2 Pollux'::varchar, 30113121::int4)::gme_tuple,
(('2025-05-12 00:00:00'::date)::timestamp, ('2025-06-23 00:00:00'::date)::timestamp, 'MoC 3.2 5TVs'::varchar, 30113122::int4)::gme_tuple,--
(('2025-03-31 00:00:00'::date)::timestamp, ('2025-05-12 00:00:00'::date)::timestamp, 'MoC 3.1 Reaver'::varchar, 30112121::int4)::gme_tuple,
(('2025-03-31 00:00:00'::date)::timestamp, ('2025-05-12 00:00:00'::date)::timestamp, 'MoC 3.1 Kafka'::varchar, 30112122::int4)::gme_tuple,--
(('2025-02-17 00:00:00'::date)::timestamp, ('2025-03-31 00:00:00'::date)::timestamp, 'MoC 3.0 True Sting'::varchar, 30111121::int4)::gme_tuple,
(('2025-02-17 00:00:00'::date)::timestamp, ('2025-03-31 00:00:00'::date)::timestamp, 'MoC 3.0 Nikador'::varchar, 30111122::int4)::gme_tuple--
]) ds
cross join public.game_mode gm
where gm.kind = 'Moc12'::gamemodekindenum
;
insert into public.game_mode_entry ("name", active_from, active_to , game_mode_id , stage_id )
select ds."name", ds."from", ds."to", gm.id, ds."stage_id"
from unnest(ARRAY[
(('2026-02-02'::date)::timestamp, ('2026-03-16'::date)::timestamp, 'AS 3.8.2 Kafka'::varchar,     420414::int4)::gme_tuple,
(('2026-02-02'::date)::timestamp, ('2026-03-16'::date)::timestamp, 'AS 3.8.2 Pollux'::varchar,     420424::int4)::gme_tuple,
(('2025-12-22'::date)::timestamp, ('2026-02-02'::date)::timestamp, 'AS 3.8.1 Argenti'::varchar,     420374::int4)::gme_tuple,
(('2025-12-22'::date)::timestamp, ('2026-02-02'::date)::timestamp, 'AS 3.8.1 5TVs'::varchar,     420364::int4)::gme_tuple,
(('2025-11-10'::date)::timestamp, ('2025-12-22'::date)::timestamp, 'AS 3.7 Stardevourer Swarm'::varchar,     420344::int4)::gme_tuple,
(('2025-11-10'::date)::timestamp, ('2025-12-22'::date)::timestamp, 'AS 3.7 Phantylia'::varchar,     420354::int4)::gme_tuple,
(('2025-09-29'::date)::timestamp, ('2025-11-10'::date)::timestamp, 'AS 3.6 Cocolia'::varchar,     420334::int4)::gme_tuple,
(('2025-09-29'::date)::timestamp, ('2025-11-10'::date)::timestamp, 'AS 3.6 Pollux'::varchar,     420324::int4)::gme_tuple,
(('2025-08-18'::date)::timestamp, ('2025-09-29'::date)::timestamp, 'AS 3.5 Hoolay'::varchar,     420314::int4)::gme_tuple,
(('2025-08-18'::date)::timestamp, ('2025-09-29'::date)::timestamp, 'AS 3.5 Feixiao'::varchar,     420304::int4)::gme_tuple,
(('2025-07-07'::date)::timestamp, ('2025-08-18'::date)::timestamp, 'AS 3.4 Reaver'::varchar,     420284::int4)::gme_tuple,
(('2025-07-07'::date)::timestamp, ('2025-08-18'::date)::timestamp, 'AS 3.4 Doomsday Beast'::varchar,     420294::int4)::gme_tuple,
(('2025-05-26'::date)::timestamp, ('2025-07-07'::date)::timestamp, 'AS 3.3 Cocolia'::varchar,     420264::int4)::gme_tuple,
(('2025-05-26'::date)::timestamp, ('2025-07-07'::date)::timestamp, 'AS 3.2 Kafka'::varchar,     420274::int4)::gme_tuple,
(('2025-04-14'::date)::timestamp, ('2025-05-26'::date)::timestamp, 'AS 3.1 Stardevourer Swarm'::varchar,     420254::int4)::gme_tuple,
(('2025-04-14'::date)::timestamp, ('2025-05-26'::date)::timestamp, 'AS 3.1 Hoolay'::varchar,     420244::int4)::gme_tuple,
(('2025-03-03'::date)::timestamp, ('2025-04-14'::date)::timestamp, 'AS 3.0 Aventurine'::varchar,     420224::int4)::gme_tuple,
(('2025-03-03'::date)::timestamp, ('2025-04-14'::date)::timestamp, 'AS 3.0 5TVs'::varchar,     420234::int4)::gme_tuple,
(('2025-01-20'::date)::timestamp, ('2025-03-03'::date)::timestamp, 'AS 2.7 Stardevourer Swarm'::varchar,     420204::int4)::gme_tuple,
(('2025-01-20'::date)::timestamp, ('2025-03-03'::date)::timestamp, 'AS 2.7 Phantylia'::varchar,     420214::int4)::gme_tuple,
(('2024-12-09'::date)::timestamp, ('2025-01-20'::date)::timestamp, 'AS 2.6 Cocolia'::varchar,     420194::int4)::gme_tuple,
(('2024-12-09'::date)::timestamp, ('2025-01-20'::date)::timestamp, 'AS 2.6 5TVs'::varchar,     420184::int4)::gme_tuple,
(('2024-10-28'::date)::timestamp, ('2024-12-09'::date)::timestamp, 'AS 2.5 Kafka'::varchar,     420174::int4)::gme_tuple,
(('2024-10-28'::date)::timestamp, ('2024-12-09'::date)::timestamp, 'AS 2.5 Septimus'::varchar,     420164::int4)::gme_tuple,
(('2024-09-16'::date)::timestamp, ('2024-10-28'::date)::timestamp, 'AS 2.4 Aventurine'::varchar,     420154::int4)::gme_tuple,
(('2024-09-16'::date)::timestamp, ('2024-10-28'::date)::timestamp, 'AS 2.4 Phantylia'::varchar,     420144::int4)::gme_tuple,
(('2024-08-05'::date)::timestamp, ('2024-09-16'::date)::timestamp, 'AS 2.3 Kafka'::varchar,     420134::int4)::gme_tuple,
(('2024-08-05'::date)::timestamp, ('2024-09-16'::date)::timestamp, 'AS 2.3 Doomsday Beast'::varchar,     420124::int4)::gme_tuple,
(('2024-06-19'::date)::timestamp, ('2024-08-05'::date)::timestamp, 'AS 2.2 Cocolia'::varchar,     420104::int4)::gme_tuple,
(('2024-06-19'::date)::timestamp, ('2024-08-05'::date)::timestamp, 'AS 2.2 Argenti'::varchar,     420114::int4)::gme_tuple
]) ds
cross join public.game_mode gm
where gm.kind = 'As'::gamemodekindenum
;

insert into public.game_mode_entry ("name", active_from, active_to , game_mode_id , stage_id )
select ds."name", ds."from", ds."to", gm.id, ds."stage_id"
from unnest(ARRAY[
	(('2025-06-09'::date)::timestamp, ('2025-07-21'::date)::timestamp, 'PF 3.3 Argenti'::varchar,	30313041::int4)::gme_tuple,
	(('2025-06-09'::date)::timestamp, ('2025-07-21'::date)::timestamp, 'PF 3.3 Swarm'::varchar,	30313042::int4)::gme_tuple,
	(('2025-07-21'::date)::timestamp, ('2025-09-01'::date)::timestamp, 'PF 3.4 Gepard'::varchar,	30314041::int4)::gme_tuple,
	(('2025-07-21'::date)::timestamp, ('2025-09-01'::date)::timestamp, 'PF 3.4 Hoolay'::varchar,	30314042::int4)::gme_tuple,
	(('2025-09-01'::date)::timestamp, ('2025-10-13'::date)::timestamp, 'PF 3.5 Bronya'::varchar,	30315041::int4)::gme_tuple,
	(('2025-09-01'::date)::timestamp, ('2025-10-13'::date)::timestamp, 'PF 3.5 Flame Reaver'::varchar,	30315042::int4)::gme_tuple,
	(('2025-10-13'::date)::timestamp, ('2025-11-24'::date)::timestamp, 'PF 3.6 Argenti'::varchar,	30316041::int4)::gme_tuple,
	(('2025-10-13'::date)::timestamp, ('2025-11-24'::date)::timestamp, 'PF 3.6 Nikador'::varchar,	30316042::int4)::gme_tuple,
	(('2025-11-24'::date)::timestamp, ('2026-01-05'::date)::timestamp, 'PF 3.7 Cocolia'::varchar,	30317041::int4)::gme_tuple,
	(('2025-11-24'::date)::timestamp, ('2026-01-05'::date)::timestamp, 'PF 3.7 Zandar'::varchar,	30317042::int4)::gme_tuple,
	(('2026-01-05'::date)::timestamp, ('2026-02-16'::date)::timestamp, 'PF 3.8 Hoolay'::varchar,	30318041::int4)::gme_tuple,
	(('2026-01-05'::date)::timestamp, ('2026-02-16'::date)::timestamp, 'PF 3.8 Ebon Deer'::varchar,	30318042::int4)::gme_tuple
]) ds
cross join public.game_mode gm
where gm.kind = 'Pf'::gamemodekindenum
;
insert into public.game_mode_entry ("name", active_from, active_to , game_mode_id , stage_id )
select ds."name", ds."from", ds."to", gm.id, ds."stage_id"
from unnest(ARRAY[
	(('2025-09-24'::date)::timestamp, ('2025-11-05'::date)::timestamp, 'AA 3.6 Zandar'::varchar,	 30501021::int4)::gme_tuple,
	(('2025-11-05'::date)::timestamp, ('2025-12-17'::date)::timestamp, 'AA 3.7 Aquila'::varchar,	 30502021::int4)::gme_tuple,
	(('2025-12-17'::date)::timestamp, ('2026-01-28'::date)::timestamp, 'AA 3.8 Septimus'::varchar,	 30503021::int4)::gme_tuple
]) ds
cross join public.game_mode gm
where gm.kind = 'Aacm'::gamemodekindenum
;
insert into public.game_mode_entry ("name", active_from, active_to , game_mode_id , stage_id )
select ds."name", ds."from", ds."to", gm.id, ds."stage_id"
from unnest(ARRAY[
	(('2025-09-24'::date)::timestamp, ('2025-11-05'::date)::timestamp, 'AA 3.6 Zandar: Plight'::varchar,	  30501022::int4)::gme_tuple,
	(('2025-11-05'::date)::timestamp, ('2025-12-17'::date)::timestamp, 'AA 3.7 Aquila: Plight'::varchar,	  30502022::int4)::gme_tuple,
	(('2025-12-17'::date)::timestamp, ('2026-01-28'::date)::timestamp, 'AA 3.8 Septimus: Plight'::varchar,	  30503022::int4)::gme_tuple
]) ds
cross join public.game_mode gm
where gm.kind = 'Aazz'::gamemodekindenum
;
insert into public.game_mode_entry ("name", active_from, active_to , game_mode_id , stage_id )
select ds."name", ds."from", ds."to", gm.id, ds."stage_id"
from unnest(ARRAY[
	(('2025-09-24'::date)::timestamp, ('2025-11-05'::date)::timestamp, 'AA 3.6 K1 Puppets Trio'::varchar,		30501011::int4)::gme_tuple,
	(('2025-11-05'::date)::timestamp, ('2025-12-17'::date)::timestamp, 'AA 3.7 K1 Aurumaton'::varchar,		    30502011::int4)::gme_tuple,
	(('2025-12-17'::date)::timestamp, ('2026-01-28'::date)::timestamp, 'AA 3.8 K1 The Ascended'::varchar,		30503011::int4)::gme_tuple
]) ds
cross join public.game_mode gm
where gm.kind = 'Aak1'::gamemodekindenum
;
insert into public.game_mode_entry ("name", active_from, active_to , game_mode_id , stage_id )
select ds."name", ds."from", ds."to", gm.id, ds."stage_id"
from unnest(ARRAY[
	(('2025-09-24'::date)::timestamp, ('2025-11-05'::date)::timestamp, 'AA 3.6 K2 Sleepie'::varchar,		    30501012::int4)::gme_tuple,
	(('2025-11-05'::date)::timestamp, ('2025-12-17'::date)::timestamp, 'AA 3.7 K2 Hoolay'::varchar,		        30502012::int4)::gme_tuple,
	(('2025-12-17'::date)::timestamp, ('2026-01-28'::date)::timestamp, 'AA 3.8 K2 True Sting'::varchar,		    30503012::int4)::gme_tuple
]) ds
cross join public.game_mode gm
where gm.kind = 'Aak2'::gamemodekindenum
;
insert into public.game_mode_entry ("name", active_from, active_to , game_mode_id , stage_id )
select ds."name", ds."from", ds."to", gm.id, ds."stage_id"
from unnest(ARRAY[
	(('2025-09-24'::date)::timestamp, ('2025-11-05'::date)::timestamp, 'AA 3.6 K3 Gryphon'::varchar,		    30501013::int4)::gme_tuple,
	(('2025-11-05'::date)::timestamp, ('2025-12-17'::date)::timestamp, 'AA 3.7 K3 5TVs'::varchar,		        30502013::int4)::gme_tuple,
	(('2025-12-17'::date)::timestamp, ('2026-01-28'::date)::timestamp, 'AA 3.8 K3 Ichor'::varchar,		        30503013::int4)::gme_tuple
]) ds
cross join public.game_mode gm
where gm.kind = 'Aak3'::gamemodekindenum
;

CREATE EXTENSION IF NOT EXISTS pg_trgm
;
drop type if exists gme_tuple;
;
;
drop function if exists find_most_fitting_lc;
create or replace function find_most_fitting_lc("search_name" text)
	returns table(id int, "name" varchar, rarity int, icon_url text, sig_of_char_id int)
	as $$
		select
			case
				when "search_name" is null or trim("search_name") = ''
					then (null::integer, null::varchar, null::int, null::text, null::int)
				else (lc.id, lc."name", lc.rarity, lc.icon_url, lc.sig_of_char_id)
			end
		from public."lightcone" lc
		order by similarity(lc.name, search_name)  desc
		limit 1
	$$
	language sql;
;
drop function if exists find_most_fitting_char;
create or replace function find_most_fitting_char("search_name" text)
	returns table(id int, "name" varchar, rarity int, icon_url text)
	as $$
		select case when "search_name" is null or trim("search_name") = '' then (null::integer, null::varchar, null::int, null::text) else (c.id, c."name", c.rarity, c.icon_url) end
		from public."char" c
		order by similarity(c.name, search_name)  desc
		limit 1
	$$
	language sql;
;
;
drop function if exists insert_run;
;
create or replace function insert_run(
	stage_name text, author_name text, video_url text, video_date timestamp,
	ltd_5star int, std_5star int, score1 int, score2 int, flags text,
	p1_char text, p1_eidolon int, p1_lc text, p1_superimp int,
	p2_char text, p2_eidolon int, p2_lc text, p2_superimp int,
	p3_char text, p3_eidolon int, p3_lc text, p3_superimp int,
	p4_char text, p4_eidolon int, p4_lc text, p4_superimp int)
	returns table(unit1_id int, unit2_id int, unit3_id int, unit4_id int, team_id int, run_id uuid, link text, author text)
	as $$
		with u1 as (
			insert into public."unit" (char_id, char_eidolon, lc_id, lc_superimposition)
			select
				 (find_most_fitting_char(p1_char)).id as charid, p1_eidolon, (find_most_fitting_lc(p1_lc)).id, p1_superimp
			where p1_char is not null and trim(p1_char) <> ''
			on conflict on CONSTRAINT "unit_uidx" do update set char_eidolon = EXCLUDED.char_eidolon
			RETURNING id
		),
		u2 as (
			insert into public."unit" (char_id, char_eidolon, lc_id, lc_superimposition)
			select
				 (find_most_fitting_char(p2_char)).id, p2_eidolon, (find_most_fitting_lc(p2_lc )).id, p2_superimp
			where p2_char is not null and trim(p2_char) <> ''
			on conflict on CONSTRAINT "unit_uidx" do update set char_eidolon = EXCLUDED.char_eidolon
			RETURNING id
		),
		u3 as (
			insert into public."unit" (char_id, char_eidolon, lc_id, lc_superimposition)
			select
				 (find_most_fitting_char(p3_char)).id, p3_eidolon, (find_most_fitting_lc(p3_lc )).id, p3_superimp
			where p3_char is not null and trim(p3_char) <> ''
			on conflict on CONSTRAINT "unit_uidx" do update set char_eidolon = EXCLUDED.char_eidolon
			RETURNING id
		),
		u4 as ( [
			insert into public."unit" (char_id, char_eidolon, lc_id, lc_superimposition)
			select
				 (find_most_fitting_char(p4_char)).id, p4_eidolon, (find_most_fitting_lc(p4_lc )).id, p4_superimp
			where p4_char is not null and trim(p4_char) <> ''
			on conflict on CONSTRAINT "unit_uidx" do update set char_eidolon = EXCLUDED.char_eidolon
			RETURNING id
		),
		team as (
			insert into public."team" ("name")
			values (p1_char||' E'||p1_eidolon||' '||p2_char||' E'||p2_eidolon||' '||p3_char||' E'||p3_eidolon||' '||p4_char||' E'||p4_eidolon)
			returning id
		),
		tul as (
			insert into public.team_unit_link (team_id , unit_id )
			select t.id, u.id
			from (
				select u1.id
				from u1
				union all
				select u2.id
				from u2
				union all
				select u3.id
				from u3
				union all
				select u4.id
				from u4
			) u
			cross join team t
		),
		gme as (
			select e.stage_id, e."name", e."active_from", e."active_to", e."game_mode_id"
			from public."game_mode_entry" e
			where e."name" ilike '%'||stage_name||'%'
			limit 1
		),
		run as (
			insert into public.run ("id", "name" , author , flags , game_mode_entry_id , link ,  primary_score, secondary_score , submitted_at , team_id )
			select gen_random_uuid (), '', author_name, case when flags is null or flags = '' then null else flags::resultflags end, gme.stage_id, video_url, score1, score2, video_date, team.id
			from gme
			cross join team
			returning *
		),
		std_cost as (
			select id, "name"
			from public."cost"
			where name ilike '%standard%'
			limit 1
		),
		ltd_cost as (
			select id, "name"
			from public."cost"
			where name ilike '%limited%'
			limit 1
		),
		std_run_cost as (
			insert into public."run_cost" ("run_id", "cost_id", "value")
			select r."id",c."id", std_5star
			from run r
			cross join std_cost c
		),
		ltd_run_cost as (
			insert into public."run_cost" ("run_id", "cost_id", "value")
			select r."id", c."id", ltd_5star
			from run r
			cross join ltd_cost c
		)
		select u1.id, u2.id, u3.id, u4.id, team.id, run.id, run.link, run.author
		from u1
		cross join u2
		cross join u3
		cross join u4
		cross join team
		cross join run
		;
	$$
	language sql;



--select *
--from insert_run(
--'aa 3.8 True Sting', '茉亭花醉月','https://www.bilibili.com/video/BV1ywBFBvEa2','	2025-12-19T22:00:00.000Z',
--3,	0,	0, null,
--'Evernight',	1,	'The Flower Remembers'	,2	,
--'Cyrene',	0,	'Memorys Curtain Never Falls',	5,
--'Remembrance MC',	6	,'Fly Into a Pink Tomorrow',	5,
--'Pela',	6,	'Resolution Shines As Pearls of Sweat',	5
--)
;
--select *
--from insert_run(
--'moc 3.3 True Sting', '8TtB', 'https://www.bilibili.com/video/BV1HCb1zQEgc', '2025-07-24T15:16:34.000Z', 8, 1, 0, null, 'Acheron', 2, '', 0 ,'Tribbie', 1, '', 0 ,'Sunday', 0, '', 0 ,'Silver Wolf', 0, '', 0
--
--)
--;select * from public.run r
--left join public.team t on r.team_id = t.id
--;
--select tul.team_id , tul.unit_id  from public.team_unit_link tul
;
--;select gen_random_uuid ()
--(
--	stage_name text, author_name text, video_url text, video_date timestamp,
--	ltd_5star int, std_5star int, score1 int, score2 int,
--	p1_char text, p1_eidolon int, p1_lc text, p1_superimp int,
--	p2_char text, p2_eidolon int, p2_lc text, p2_superimp int,
--	p3_char text, p3_eidolon int, p3_lc text, p3_superimp int,
--	p4_char text, p4_eidolon int, p4_lc text, p4_superimp int)

--create type tuopa_unit as (
--	char_name text,
--	char_eid int,
--	lc_name text,
--	lc_eid int
--)
--



--;			select e.stage_id, e."name", e."active_from", e."active_to", e."game_mode_id"
--			from public."game_mode_entry" e
--			where e."name" ilike '%'||'pf 3.7 Zandar'||'%'
--			limit 1
--			;


--as 3.6 Cocolia
--as 3.6 Pollux
--as 3.7 Phantylia
--as 3.7 Stardevourer Swarm
--as 3.8.1 5TVs
--as 3.8.1 Argenti
--moc 3.3 True Sting
--moc 3.4 Aventurine
--moc 3.5 Gepard
--moc 3.5 Zandar
--moc 3.6 Flame Reaver
--moc 3.6 Ichor
--moc 3.7 Hoolay
--moc 3.7 Sam
--pf 3.6 Argenti
--pf 3.6 Nikador
--pf 3.7 Cocolia
--pf 3.7 Zandar


--select * from find_most_fitting_lc('Dance');
--select d.id from find_most_fitting_char('') d;
--select * from public.game_mode_entry gme ;
--select * from public.char c ;
--select * from public.game_mode gm ;
--select gme.name, gme.stage_id , count(1)
--from public."game_mode_entry" gme
--left join public."run" r on r.game_mode_entry_id = gme.stage_id
--group by gme.name, gme.stage_id
--having count(1) > 1
--order by gme.name
--;
--
--select * from insert_run('moc 3.3 True Sting', '伊奎赛因iqueesane', 'https://www.bilibili.com/video/BV11u3gzjEVP', '2025-07-03T17:07:56.000Z', 6, 0, 0, null, '', 'Qingque', 5, '', 0 ,'Sparkle', 2, '', 0 ,'Tribbie', 1, '', 0 ,'Trailblazer (Remembrance)', 6, '', 0)

;

--select *
--from team t
--join run r on r.team_id = t.id
--where t."name"='Qingque E6 Sparkle E2 Tribbie E1 Trailblazer (Remembrance) E6'
--select * from public."run" gme where flags is not null ;--gme.game_mode_entry_id  = 30117121;
--select count(1) from public.char c;
----select (20260119::date)
------; select CURRENT_TIMESTAMP --2026-01-05 15:46:55.154 +0300
----;( 'Unknown', 'Moc12', 'Pf', 'As', 'Aak1', 'Aak2', 'Aak3', 'Aacm', 'Aazz');
----;('Cycles', 'Av', 'Score');
----select * from public.resultflags
--
--alter type public.resultflags add value 'nohit';
--;
--select ''::resultflags
--update public.game_mode gm set "name" = 'AA lv120 Plight' where kind='Aazz'::gamemodekindenum;

"""
