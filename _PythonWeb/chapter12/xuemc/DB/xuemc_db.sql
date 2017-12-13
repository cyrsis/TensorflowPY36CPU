Password: 
--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

--
-- Name: account_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE account_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.account_id_seq OWNER TO postgres;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: account; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE account (
    id integer DEFAULT nextval('account_id_seq'::regclass) NOT NULL,
    username character varying(100) DEFAULT NULL::character varying,
    password character varying(510) DEFAULT NULL::character varying,
    name character varying(40) DEFAULT NULL::character varying,
    telephone character varying(100) DEFAULT NULL::character varying,
    role integer DEFAULT 0,
    flag_telephone integer,
    checkcode character varying(50),
    source character varying(20),
    dtcreate timestamp without time zone
);


ALTER TABLE public.account OWNER TO postgres;

--
-- Name: COLUMN account.role; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN account.role IS 'COMMENT ''0:normal, 1: admin''';


--
-- Name: advert; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE advert (
    id integer NOT NULL,
    title character varying(200),
    website character varying(200),
    image_file character varying(200)
);


ALTER TABLE public.advert OWNER TO postgres;

--
-- Name: advert_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE advert_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.advert_id_seq OWNER TO postgres;

--
-- Name: advert_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE advert_id_seq OWNED BY advert.id;


--
-- Name: agespan_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE agespan_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.agespan_id_seq OWNER TO postgres;

--
-- Name: agespan; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE agespan (
    id integer DEFAULT nextval('agespan_id_seq'::regclass) NOT NULL,
    name character varying(100) DEFAULT NULL::character varying,
    fromage integer,
    toage integer
);


ALTER TABLE public.agespan OWNER TO postgres;

--
-- Name: area_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE area_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.area_id_seq OWNER TO postgres;

--
-- Name: area; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE area (
    id integer DEFAULT nextval('area_id_seq'::regclass) NOT NULL,
    name character varying(100) DEFAULT NULL::character varying
);


ALTER TABLE public.area OWNER TO postgres;

--
-- Name: bulletin_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE bulletin_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.bulletin_id_seq OWNER TO postgres;

--
-- Name: bulletin; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE bulletin (
    id integer DEFAULT nextval('bulletin_id_seq'::regclass) NOT NULL,
    dt timestamp with time zone,
    title character varying(200) DEFAULT NULL::character varying,
    content character varying(10000) DEFAULT NULL::character varying,
    valid integer DEFAULT 1,
    source character varying(70),
    author character varying(70)
);


ALTER TABLE public.bulletin OWNER TO postgres;

--
-- Name: bulletinimage; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE bulletinimage (
    id integer NOT NULL,
    bulletin_id integer,
    file character varying(500)
);


ALTER TABLE public.bulletinimage OWNER TO postgres;

--
-- Name: bulletinimage_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE bulletinimage_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.bulletinimage_id_seq OWNER TO postgres;

--
-- Name: bulletinimage_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE bulletinimage_id_seq OWNED BY bulletinimage.id;


--
-- Name: feature_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE feature_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.feature_id_seq OWNER TO postgres;

--
-- Name: feature; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE feature (
    id integer DEFAULT nextval('feature_id_seq'::regclass) NOT NULL,
    name character varying(100) DEFAULT NULL::character varying
);


ALTER TABLE public.feature OWNER TO postgres;

--
-- Name: feetype_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE feetype_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.feetype_id_seq OWNER TO postgres;

--
-- Name: feetype; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE feetype (
    id integer DEFAULT nextval('feetype_id_seq'::regclass) NOT NULL,
    name character varying(400) DEFAULT NULL::character varying
);


ALTER TABLE public.feetype OWNER TO postgres;

--
-- Name: institution_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE institution_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.institution_id_seq OWNER TO postgres;

--
-- Name: institution; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE institution (
    id integer DEFAULT nextval('institution_id_seq'::regclass) NOT NULL,
    name character varying(200) DEFAULT NULL::character varying,
    area_id integer,
    agespan_id integer,
    address character varying(200) DEFAULT NULL::character varying,
    location character varying(200) DEFAULT NULL::character varying,
    website character varying(200) DEFAULT NULL::character varying,
    telephone character varying(200) DEFAULT NULL::character varying,
    feedesc character varying(200) DEFAULT NULL::character varying,
    feetype_id integer,
    longitude real,
    latitude real,
    featuredesc character varying(400) DEFAULT NULL::character varying,
    feature_id integer,
    timeopen timestamp without time zone,
    timeclose timestamp without time zone
);


ALTER TABLE public.institution OWNER TO postgres;

--
-- Name: institution_feature; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE institution_feature (
    institution_id integer NOT NULL,
    feature_id integer NOT NULL
);


ALTER TABLE public.institution_feature OWNER TO postgres;

--
-- Name: institutionimage_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE institutionimage_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.institutionimage_id_seq OWNER TO postgres;

--
-- Name: institutionimage; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE institutionimage (
    id integer DEFAULT nextval('institutionimage_id_seq'::regclass) NOT NULL,
    institution_id integer,
    file character varying(1000) DEFAULT NULL::character varying
);


ALTER TABLE public.institutionimage OWNER TO postgres;

--
-- Name: school_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE school_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.school_id_seq OWNER TO postgres;

--
-- Name: school; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE school (
    id integer DEFAULT nextval('school_id_seq'::regclass) NOT NULL,
    name character varying(200) DEFAULT NULL::character varying,
    area_id integer,
    teachdesc character varying(4000) DEFAULT NULL::character varying,
    address character varying(200) DEFAULT NULL::character varying,
    schooltype_id integer,
    website character varying(200) DEFAULT NULL::character varying,
    leisure character varying(2000) DEFAULT NULL::character varying,
    threashold character varying(2000) DEFAULT NULL::character varying,
    partner character varying(200) DEFAULT NULL::character varying,
    artsource character varying(2000) DEFAULT NULL::character varying,
    feedesc character varying(200) DEFAULT NULL::character varying,
    distinguish character varying(2000) DEFAULT NULL::character varying,
    longitude real,
    latitude real,
    feature_id integer
);


ALTER TABLE public.school OWNER TO postgres;

--
-- Name: school_feature; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE school_feature (
    school_id integer NOT NULL,
    feature_id integer NOT NULL
);


ALTER TABLE public.school_feature OWNER TO postgres;

--
-- Name: schoolimage_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE schoolimage_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.schoolimage_id_seq OWNER TO postgres;

--
-- Name: schoolimage; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE schoolimage (
    id integer DEFAULT nextval('schoolimage_id_seq'::regclass) NOT NULL,
    school_id integer,
    file character varying(1000) DEFAULT NULL::character varying
);


ALTER TABLE public.schoolimage OWNER TO postgres;

--
-- Name: schooltype_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE schooltype_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.schooltype_id_seq OWNER TO postgres;

--
-- Name: schooltype; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE schooltype (
    id integer DEFAULT nextval('schooltype_id_seq'::regclass) NOT NULL,
    name character varying(100) DEFAULT NULL::character varying
);


ALTER TABLE public.schooltype OWNER TO postgres;

--
-- Name: terminal_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE terminal_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.terminal_id_seq OWNER TO postgres;

--
-- Name: terminal; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE terminal (
    id integer DEFAULT nextval('terminal_id_seq'::regclass) NOT NULL,
    account_id integer,
    type integer,
    code character varying(510) DEFAULT NULL::character varying
);


ALTER TABLE public.terminal OWNER TO postgres;

--
-- Name: test; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE test (
    "user" character varying(50) NOT NULL,
    tt timestamp without time zone
);


ALTER TABLE public.test OWNER TO postgres;

--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY advert ALTER COLUMN id SET DEFAULT nextval('advert_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY bulletinimage ALTER COLUMN id SET DEFAULT nextval('bulletinimage_id_seq'::regclass);


--
-- Data for Name: account; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY account (id, username, password, name, telephone, role, flag_telephone, checkcode, source, dtcreate) FROM stdin;
\.


--
-- Name: account_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('account_id_seq', 1, false);


--
-- Data for Name: advert; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY advert (id, title, website, image_file) FROM stdin;
\.


--
-- Name: advert_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('advert_id_seq', 1, false);


--
-- Data for Name: agespan; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY agespan (id, name, fromage, toage) FROM stdin;
1	小學生	6	13
2	幼兒	3	10
3	成人	18	120
4	小學生及國中生	6	18
\.


--
-- Name: agespan_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('agespan_id_seq', 4, true);


--
-- Data for Name: area; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY area (id, name) FROM stdin;
2	徐匯區
3	黃浦區
4	盧灣區
5	靜安區
6	長寧區
7	閔行區
8	楊浦區
9	普陀區
10	虹口區
11	寶山區
12	閘北區
13	松江區
14	嘉定區
15	青浦區
16	奉賢區
17	金山區
18	崇明縣
1	浦東新區
\.


--
-- Name: area_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('area_id_seq', 18, true);


--
-- Data for Name: bulletin; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY bulletin (id, dt, title, content, valid, source, author) FROM stdin;
1	2015-06-24 21:31:28+08	2015年全區優秀學生、“三好學生”、優秀學生干部、先進班集體名單公示的知會	各市教育局，各高等學校，中等職業學校：	1	\N	\N
2	2015-06-25 21:31:28+08	國土資源部擬聘請的第四屆國家特邀國土資源監察專員公示知會	v234	1	\N	\N
3	2015-06-25 21:31:28+08	關於征求對《國土資源“十三五”科學和技術發展規劃》（征求意見稿）意見的函	dfg	1	\N	\N
4	2015-06-25 21:31:28+08	“拍客日記”國土資源公益微視訊網路征集活動啟事	234	1	\N	\N
5	2015-06-25 21:31:28+08	國土資源部辦公廳關於推薦“十二五”科技與國際合作先進集體、先進個人的知會	fg	1	\N	\N
6	2015-06-25 21:31:28+08	關於2015年公開選取礦業權評估機構的函	sdf	1	\N	\N
7	2015-06-25 21:31:28+08	“像保護大熊貓一樣保護耕地”主旨散文大賽征稿啟事	234	1	\N	\N
8	2015-06-25 21:31:28+08	中國礦業權評估師協會關於公開招聘工作人員的啟事	sdfsd	1	\N	\N
9	2015-06-25 21:31:28+08	\t2015年度國土資源科學技術獎申報專案公示	sdfsdf	1	\N	\N
10	2015-06-25 21:31:28+08	(NULL)國土資源部關於發布《水文地質調查規範（1：50000）》等4項產業標准的公告	sdfg	1	\N	\N
11	2015-06-25 21:31:28+08	2015年度國土資源標准制修訂工作計劃公示	dfgfdg	1	\N	\N
12	2015-06-25 21:31:28+08	國土資源部關於取消國家地質公園規劃審核等事項的公告	dfgdfg	1	\N	\N
13	2015-06-25 21:31:28+08	國土資源部關於發布《重力調查技術規範（1：50000）》等4項產業標准的公告	dfg	1	\N	\N
14	2015-06-25 21:31:28+08	2015年度航空物探調查專案飛行工作承擔人競爭性談判優選結果公告	dfg	1	\N	\N
15	2015-06-25 21:31:28+08	人力資源社會保障部 國土資源部關於評選全國國土資源管理系統先進集體和先進工作者的	dfg	1	\N	\N
16	2015-06-25 21:31:28+08	《晉城藍焰煤業股份有限公司鳳凰山礦礦山地質環境保護與還原治理專案》等18個“專案”透過審查的公告	dfg	1	\N	\N
17	2015-06-25 21:31:28+08	\t2014年度國土資源政務訊息網上公開執行情況檢查結果	hg	1	\N	\N
18	2015-06-25 21:31:28+08	國土資源部辦公廳關於開展第25個全國“土地日”主旨宣傳周活動的知會	fdg	1	\N	\N
19	2015-06-25 21:31:28+08	中華人民共和國國土資源部令	dgf	1	\N	\N
20	2015-06-25 21:31:28+08	2015年1季度國土資源部評審備案礦產資源儲量成果訊息情況	sdf	1	\N	\N
21	2015-06-25 21:31:28+08	國土資源部辦公廳關於實行規範性檔案 “三統一”制度的知會	sdf	1	\N	\N
\.


--
-- Name: bulletin_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('bulletin_id_seq', 21, true);


--
-- Data for Name: bulletinimage; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY bulletinimage (id, bulletin_id, file) FROM stdin;
\.


--
-- Name: bulletinimage_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('bulletinimage_id_seq', 1, false);


--
-- Data for Name: feature; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY feature (id, name) FROM stdin;
0	
1	藝術（聲樂、樂器、繪畫、舞蹈）
2	語系（英語、小語種）
3	體育
4	課外輔導（語文、奧數）
5	思維邏輯
6	國學（書法、國畫、圍棋、蒙學）
\.


--
-- Name: feature_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('feature_id_seq', 2, true);


--
-- Data for Name: feetype; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY feetype (id, name) FROM stdin;
1	按時間收費
2	按等級收費
\.


--
-- Name: feetype_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('feetype_id_seq', 2, true);


--
-- Data for Name: institution; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY institution (id, name, area_id, agespan_id, address, location, website, telephone, feedesc, feetype_id, longitude, latitude, featuredesc, feature_id, timeopen, timeclose) FROM stdin;
1	韋博國際英語	2	3	衡山路922號建匯大廈33層	徐家匯中心	http://www.webi.com.cn	400-720-9090	每小時2元	1	\N	\N	（實用英語、職場英語、雅思、托福、SAT等等）	0	1999-01-01 08:00:00	1999-01-01 22:00:00
2	東書房	5	1	張楊路500號華潤時代廣場6樓（接近浦東南路，八佰伴對面）	華潤中心	http://www.dongshufang.cn/	400-870-2227	1、按等級收費，每個等級6個月；2、按時間收費，不限等級；	2	\N	\N	（古箏、圍棋、書法、國畫）	0	1999-01-01 08:00:00	\N
\.


--
-- Data for Name: institution_feature; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY institution_feature (institution_id, feature_id) FROM stdin;
1	1
2	2
\.


--
-- Name: institution_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('institution_id_seq', 2, true);


--
-- Data for Name: institutionimage; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY institutionimage (id, institution_id, file) FROM stdin;
\.


--
-- Name: institutionimage_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('institutionimage_id_seq', 1, false);


--
-- Data for Name: school; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY school (id, name, area_id, teachdesc, address, schooltype_id, website, leisure, threashold, partner, artsource, feedesc, distinguish, longitude, latitude, feature_id) FROM stdin;
14	上海市黃浦區盧灣區中心小學	3	校長姓名：陳瑾\r\n教職工119人，其中教師104人，高、中級職稱教師占在崗教師的57.1%，大專及以上學歷的教師占86.7%，大本占15.3%，區命名的校級以上骨干教師占38.8%，其中區學科帶頭人一名，區青年學科帶頭人2名，區級骨干教師13人。	茂名南路175號/皋蘭路20號	2	http://www2.ezx.lwwdu.sh.cn/	我以青春鑄黨旗、讀《中國反貪調查》有感、時刻敲響安全警鍾、走進書法天地、增加閱讀興趣、經驗讀書快樂、增加閱讀興趣、經驗讀書快樂。	茂名、香山、思南、水嘉、瑞雪、建德	上海市啟秀實驗國中		公費		121.46891	31.2204514	\N
15	上海市黃浦區回民小學	3	校長姓名：倪玉琴\r\n專職教師42人	聚奎街50號	2		新藝隊	龍潭、光啟、四新			公費		121.503227	31.2296925	\N
16	上海市黃浦區盧灣—中心小學	3	校長姓名：程華\r\n國中進階教師3人，小學進階教師75人，占教師總數61.4%，從教師學歷階層看：進修研究生課程的有1人；大專本科學歷（含在讀）共有25人；35歲以下青年教師全部達到大專學歷	淡水路450號	2	http://www.yzx.lwedu.sh.cn/	尊敬長輩 微笑重陽、加強安全意識 做到未雨綢繆、我愛我校 創意無限、家校攜手行 幸福暖人心。	建二、建四、建五、建六、復三、順六、建三	興業國中		公費		121.480553	31.217865	\N
17	上海市實驗小學	3	校長姓名：楊榮\r\n現有120多名教職工，400多名退休教師。其中現職國中進階教師12名，先後有7名教師列入全國、上海市的名師培養物件。	人民路706號	2	http://shy.hpe.cn	真愛生命，消防安全、迷夢，助夢，圓夢、漂流角，倡文明、學分享、綠色軍營 難忘之旅。	露香、大境、淮海、阜春、長生、同慶	上海市敬業初級國中		公費		121.491791	31.2341461	\N
21	上海市實驗小學	3	校長姓名：楊榮\r\n現有120多名教職工，400多名退休教師。其中現職國中進階教師12名，先後有7名教師列入全國、上海市的名師培養物件。	人民路706號	2	http://shy.hpe.cn	真愛生命，消防安全、迷夢，助夢，圓夢、漂流角，倡文明、學分享、綠色軍營 難忘之旅。	露香、大境、淮海、阜春、長生、同慶	上海市敬業初級國中		公費		121.4879	31.2491627	\N
18	上海市北京東路小學	3	"校長姓名：張燁 \r\n特級教師、市區級骨干教師十多人，小內有首席教師3人，學科帶頭人6人，具有小學進階教師職稱的占最前線教師總數的80%，在職45歲以下教師大專及大專以上學歷達到100%。"	北京東路261號	2	http://bj.hpe.sh.cn/	敢於夢想，敢於追夢、在中華歷史文化中遨游、大作家與小讀者見面會，小荷才露尖尖角，有朝一日定綻放、泳池戲水忙，家長樂開懷	無錫、虎丘、北京、中北、龍泉、牛莊、雲中、廈門、貴州	上海市浦光國中		公費		121.491402	31.2461414	\N
22	上海市北京東路小學	3	校長姓名：張燁 \r\n特級教師、市區級骨干教師十多人，小內有首席教師3人，學科帶頭人6人，具有小學進階教師職稱的占最前線教師總數的80%，在職45歲以下教師大專及大專以上學歷達到100%。	北京東路261號	2	http://bj.hpe.sh.cn/	敢於夢想，敢於追夢、在中華歷史文化中遨游、大作家與小讀者見面會，小荷才露尖尖角，有朝一日定綻放、泳池戲水忙，家長樂開懷	無錫、虎丘、北京、中北、龍泉、牛莊、雲中、廈門、貴州	上海市浦光國中		公費		121.491402	31.2461491	\N
20	上海市黃浦區重慶北路小學	3	學校擁有一批素質好、能力強、業務精、善思考、肯奉獻的教師，其中國中進階教師3人，小學進階教師28人，區、校級骨干教師6人，中國共產黨員7人。	大沽路262號	2	http://chongb.hpe.cn/	墨香溢校園、在創造的道路上前行	均樂、振興、江陰、順天村	上海市儲能國中		公費		121.475662	31.2319813	\N
19	上海市黃浦區盧灣三中心小學	3	教師隊伍，100%大專學歷，本科學歷64.4%，研究生5%，70%以上的教師具有中、進階職稱。	嵩山路69號	2	http://www.szx.lwedu.sh.cn/	習慣第一 輕松過關、我眼中的幸福家庭、改善研讀模式、以互助促共同進步、科學思維模式在自然學科中扎根	瀏河、新華、大華、志成、星平、景安、瑞華	比樂國中		公費		121.482208	31.229105	\N
23	上海市黃浦區四川南路小學	3	"校長姓名：樓麗霞\r\n學校教職員工共74人，其中小學進階教師37人，占總人數的50%，小學一級教師27人，占36%，小學二級教師2人，占3%，還有7人為職員及工勤人員。"	四川南路36號	2	http://sinan.hpe.cn/	讓環保走進我們的生活、我與淘寶手牽手，快樂閱讀齊分享、我們在快樂地前行	永勝、盛澤、中山、寶興、永安、雲南、福南、金陵、漢口			公費		121.497261	31.2365036	\N
24	上海師范專科學校附屬小學	3	"校長姓名：韓新文\r\n學校有一支年富力強的教師，在職教師平均年齡34歲，碩士學歷6.7%，本科學歷70.1%，進階職稱占3.3%，中級職稱占67.3%。目前教師隊伍中區青年學科帶頭人、區骨干教師占15%、校級骨干教師13%。優秀的教師隊伍增強了學校可持續發展的綜合實力。2006年學年度，學校共有30名教師參加各級各類別教育、教學比賽獲獎，占教師總比54%。"	局門路478號	2	http://www.szfx.lwedu.sh.cn/MPS/Default.aspx	沐科普陽光 啟科技夢想、創意畫單字，創意吳極限、排球之星，明日之光、“考場”成舞台“學生”變主角、切磋球藝、展現自我	麗園、桑城、中二、橋一、橋二			公費		121.488846	31.2080021	\N
25	上海市黃浦區蓬萊路第二小學	3	校長姓名：季萍\r\n學校在編在崗教師82名，其中國中進階7名，市級名師培養物件3名，區學科帶頭人2名，區骨干教師4名。	蓬萊路225號	2	http://www.xxpengl.com.cn/	故事情境國中語文 研讀準備期多歡樂、暑假足球夏令營、蓬二學生繪制團扇送清涼、“伴我聰慧成長”演講比賽，開展“郵遞明信片·分享幸福行”活動	文廟、淨土、小桃園、艾家弄	上海市第十國中		公費		121.496666	31.2234573	\N
27	上海市黃浦區新凌小學	3	在崗教師58人，其中小學進階教師46人，青年教師占教師總數的72.41%，青年教師44.2%獲得大專學歷，30.2%獲得大本學歷，23.3%教師大本在讀。學校有6位教師是區學科中心群組成員，區骨干教師1位。	西凌家宅路90弄33號	2	http://xinling.cn.class.uschoolnet.com/	雛鷹在飛翔、榮譽之花	黃浦新苑、民立、保屯、瞿二、瞿四、製造、徽寧、三門、西一、西二、西三			公費		121.493134	31.2103176	\N
28	上海黃浦區裘錦實驗學校	3	校長姓名：沈位岡\r\n在校任職的教師100%達到大專以上學歷，歷屆被推薦評選為區學科帶頭和市區級骨干教師10名；參加區名師工作室研讀教育訓練7人；近兩年20余名教師榮獲全國、市、區先進榮譽稱號：15名教師榮獲課堂教育教學評比一、二、三等獎。	新橋路55號	2	http://www.qjq.hpe.cn/	探尋奇妙“海”世界，綠色天使秋游行、老少重陽，別樣對日、零起點研討，全方位實作、參觀四大會址，銘記黨的歷史	新橋、三德、承興、福海、福瑞			公費		121.472084	31.2458973	\N
13	上海市黃浦區徽寧路第三小學	3	校長姓名：朱惠芳\r\n在崗教職工100余名。	徽寧路216號	2	http://huining.hpe.cn/	“活力徽三凝聚歡樂”第三屆師生運動會、豐富業余生活提昇藝術修養。在春游活動中培養愛國情懷、徜徉藝術的殿堂，啟發藝術素養	明日星城、陸迎、中福一、中福二、海西、車中、新村、益元、迎助、普益	上海市市南國中		公費		121.499191	31.2169991	\N
29	上外·黃浦外國語小學	3	在發展外語特色的執行緒中，學校不斷改善師資，引進人才。逐步建構起一支理念新，素質高，專業精神的教師隊伍。其中本科學歷及在讀本科的教師占最前線教師總人數的80%。	半淞園路609號	2	hettp://flps.hpe.sh.cn	小小農家了之冬瓜、南瓜大豐收、幸福耕耘 夢想成真、觀看木偶劇，感受傳統文化、研讀西餐禮儀，經驗西餐文化、人人參與 玩轉籃球	高雄、市民、耀江花園			公費		121.500465	31.2052536	\N
30	上海市黃浦區盧灣海華小學	3	校教職工共57人，其中有多名區青年學科帶頭人及骨干教師，中進階及進階教師占全校74%，在歷年全國、市區等教學比賽中，一批中青年教師脫穎而出，獲一、二、三等獎。	瑞金南路85號	2	http://www.haihua.lwedu.sh.cn/	生命科技節、陽光英語節、活力體育節、成長讀書節、多彩藝術節	大同、錦海、南塘、瑞楠、斜土、打浦、海悅	盧灣國中		公費		106.722832	26.5710735	\N
31	上海市黃浦區巨鹿路第一小學	3	校長姓名：樓海鳳\r\n教師學歷96%大專學歷，65%本科學歷。國中進階教師12%，區級以上骨干教師數36%，校級以上骨干占教師數60%。	南昌路366號	2	http://www.jy.lwedu.sh.cn/newsite	英語節、走進經典，感受藝術之美、陽光 體育，健康成長、垃圾分類別大家說	南昌、延中、巨鹿、錦江\r\n			公費		121.466736	31.2216606	\N
32	上海市黃浦區瞿溪路小學	3	學校現有在編教職工50名，在崗教職工38人，其中國中進階教師1人，占教書數2.7%，小學進階27人，占教師數73%，大學學歷27人，占73%。	瞿溪路1117號	2	http://www.quxi.lwedu.sh.cn/	“唱響新童謠，快樂伴我行”八榮八恥特別行動；“六心”小天帶著微笑送出禮儀之花、“文明交通在我腳下”倡議書、“新春愛心行動”紅領巾“手拉手”結對互助送溫暖、“一份小禮物、一顆大愛心”“六一”大型義賣籌款、“送上一顆愛心”慰問孤老活動、紅領巾文明尋訪團活動“發現靚麗盧灣”小小攝影師活動、“中國人過中國節”民族活動、“驕傲啊，中國人”讀書活動	瞿西、瞿中、瞿南\r\n	盧灣區教師進修學院附屬中山學校		公費		121.479988	31.2048149	\N
26	上海市黃浦區七色花小學	3	學校注重打造一支具有較高師德修養與專業素養的復合型教師隊伍。其中100%的教師具有大專及大學本科學歷，校級、區級骨干教師占30%，上海市名師培養專案教師1名。學校有多位教師在全國、市、區各類別教育教學比賽中獲得殊榮。	雁蕩路56弄46號	2	http://www.qsh.lwedu.sh.cn/	藝術節、科技節、英語奧斯卡、七彩舞台、“小小地球村”藝術人文展示活動、為支援貧困地區的義演義賣活動、親子迎新運動會	雁蕩、長樂、淮中、瑞成			公費		121.475754	31.2261086	\N
33	上海黃浦區瑞金二路小學	3	"校長姓名：王平\r\n30多名教職員工，其中小學進階教師16名，一級教師13名，區骨干教師2名，校骨干教師4名"\r\n	瑞金二路215號	2	http://www.ruier.lwedu.sh.cn/	單字接龍比比看，英語研讀真有趣、啄木鳥在行動、陽光體育，文武平行、人人都是小畫家、灌籃高手\r\n	建中、泰康、陝建、肇東\r\n			公費		121.473351	31.2143211	\N
38	上海市長寧區北三幼兒園	6	園長：朱芸             具有一批經驗豐富、教學理念先進的骨干教師，全園教師本科及大專畢業達100%，形成了以教學經驗豐富的高素質、高學歷、充滿活力的教師隊伍	上海市長寧區新涇一村135號	1	http://3101050168.age06.com/310105/527/	課余活動室	"1.天山路:88弄                        2.長寧路:3229弄   \r\n3.哈密路:100弄                       4.蒲淞北路                          5.天山西路:80弄、350弄  \r\n6.北大街:31弄                       7.北漁路:28弄                        8.金鍾路:255弄、340弄\r\n9.新涇一村                           10.劍河路:60弄、200-260號             11.平塘路:222弄   \r\n12.北翟路:75弄、105弄、163弄        13.清池路:110弄"\t			幼管費：175元/月                        伙食費：9元/人/天               點心費：4元/人/天		121.376068	31.2233372	\N
36	上海市黃浦區復興東路第三小學	3	校長：胡愛珠\r\n全校共有教職員工67名，其中管理人員3名，教師62名，工人2名。他們都在各自的教育、教學領域中發揮著不小的作用，67名教職員工中，碩士研究生1名，占教職員工的1%，本科學歷39名，占教職員工的58%，大專學歷22名，占教職員工的33%,中專及以下學歷5名，占教職員工的8%。40歲以下教師56名，占全校教職工84%，進階職稱3名，中級職稱41名，初級職稱23名，全校教職員工中，區級骨干教師2名，校級骨干教師6名，約有82%獲區級以上榮譽稱號，論文在區級以上雜誌發表，或在課堂教學評比中獲區級以上等地獎。	復興東路949號（復興東路莊家街）	2	http://www.fxdl.hpe.cn/	校徽設計我做主，一起來跑步章，讓幸福詩情畫意，到手牽小手，綠從心開始，主任為樂小雷鋒	肇方、會稽、泰瑞、方西、太陽都市	李惠利國中		公費		121.493584	31.2265186	\N
45	上海市長寧區哈密路幼兒園	4	園長：孫寶娣           在編教職工35名，另有1名派遣制教師、4名派遣制保育員、11名臨時工，分別擔任保育員、營養員、夜班門衛等職;以及保安公司委派的保安人員4名，共計51人。	哈密路2016、2024號/迎賓三路128號	1	http://3101050174.age06.com/310105/530/	幼管費：225元/月；外籍：1300月/月；伙食費：9元/人/天；點心費：4元/人/天	總園： \r\n1.龍溪路:1-219 號\r\n2.虹橋路:2121-2419 號\r\n3.程橋一村、程橋二村\r\n4.程家橋路:1-150 號\r\n5.虹井路:800-1000 號\r\n6.劍河路:2001 弄\r\n7.哈密路（單）:1713-2079 號 哈密路（雙）:1800-2054 號 \r\n機場分園: \r\n1.機場新村、上航新村\r\n2.滬青平公路:18 弄\r\n3.虹橋路:2538 弄 					121.376701	31.1972408	\N
37	上海市長寧區仙一幼兒園	6	園長：金瑩             教職工人數36人，園長1名，保教主任1名，教師25名，其他教職工5人，除回聘後勤外，其他學歷都已大專以上，13名教師已獲本科學歷，其他5位教師本科在讀。青年教師占教師55%，中年教師占45%，幼兒進階教師13名	上海市長寧區仙霞路435弄7號	1	http://3101050163.age06.com/310105/522/	03早教活動                 經常性開放活動              民族文化的藝術活動	"1.仙霞路：410弄—500弄                        2.茅台路：455弄\r\n3.芙蓉江路：62弄—150弄 （雙弄）     4.水城路：90號—500弄（雙號、弄）\r\n5.虹古路：208弄、270弄\r\n6.榮華居委一期：１倫敦廣場（古北路1000號）；   ２馬賽花園（榮華東道79、80、102弄）；\r\n３巴黎花園、巴黎經典（榮華東道119弄）；            ４維也納花園（榮華東道106、108、110、112號）；\r\n５維多利亞大廈（榮華東道96、98、116、128號）；                           ６88大廈（榮華東道88號）\r\n7.榮華居委三期：                     １古北新苑（古北路1398弄）；         ２黃金豪園（黃金城道770、777號）；\r\n３四季晶園（水城南路16弄）；         ４羅馬花園（榮華東道8弄）；\r\n５鹿特丹花園（榮華東道19弄）；       ６裡昂花園（榮華東道59、60弄）；\r\n７雅典花園（榮華東道46、48、50號）"\t			幼管費：225元/月     外籍：1300月/月          伙食費：9元/人/天               點心費：4元/人/天		121.400002	31.2099991	\N
39	上海市長寧區實驗幼兒園	6	"園長：周劍\r\n常務副園長兼長寧實驗幼兒園聯合黨支部書記：鄭慧敏\r\n副園長兼副書記：張建紅\r\n副園長：奚玨\r\n工會主席：楊蓓蕾\r\n園長助理：劉燕琳        幼兒園圍繞課程改革和創新開展了一系列的教育科學研究，孵化出一支優秀的教師團隊，在課程的研究與開發方面有著自己獨特的見解。曾連續兩次被評為上海市教育科學研究先進集體。“幼兒園活動區教育模式的研究”、“幼兒園互動式主旨活動的理性思考與實作探索”、“2—3嬰幼兒情境化活動環境的實作與研究”等課題均在市級教育科學研究成果評比中獲等第獎，其研究成果匯編成《活動區活動教師手冊》和《嫣紅奼紫開遍-——幼兒園綜合性主旨教育新創版》出版"	上海市長寧區雲霧山路135號	1	http://cnsyyey.age06.com/310105/67/		電腦派位	實驗小學		幼管費：700元/月     外籍：1300月/月          伙食費：9元/人/天               點心費：4元/人/天		121.410004	31.2199993	\N
48	上海市長寧區武夷路幼兒園	6	園長：張潔	武夷路95弄19號	1	http://3101050147.age06.com/310105/507/		1.  延安西路(單號):485-1395號；延安西路(雙號):902-1146號、1350號                     \r\n2. 江蘇路(單號):507-835號；江蘇路(雙號):470-878號 \r\n3. 武夷路:17-373號\r\n4. 利西路:2-307號\r\n5. 昭化路:12-357號\r\n6. 昭化東路:52-209號              \r\n7. 宣化路(單號):1-317號\r\n8. 定西路(雙號):906-1328號  \r\n9. 曹家堰路、張家宅、西諸安濱路\r\n10.華山路:800-1136弄\r\n11.安西路:397-676號\r\n12.安化路:1-360號\r\n13.鎮寧路(單號):9-99號			幼管費：175元/月；伙食費：9元/人/天；點心費：4元/人/天		121.435776	31.2206669	\N
42	上海市黃浦區報童小學	3	校長：余敏\r\n學校已擁有一流的師資力量，教師學歷都達到大專以上，國中進階教師、區學科帶頭人、小學進階教師占92%。	山西南路35號	2	http://baotong.hpe.cn/info/frame_index.asp?info_class_id=182&height=600&width=800		新增、山西、昭通、北海、瑞福、小花園、平望	上海市應昌期圍棋學校		公費		121.489746	31.2407913	\N
49	上海黃浦區曹光彪小學	3	校長姓名：金建中\r\n在編教職工86名，其中教師79名，91%的教師具有大專以上的學歷，80%的教師具有中、進階專業技術職稱。	長沙路1號（長沙路牯嶺路）	2	http://cgb.hpe.cn	陽光、微笑、成長、彩虹橋、學科學、動手玩 全家一起“秀”、讓童年更有意義、放慢戒指重習慣 紮實起步教撰寫	長江、定興、新昌	格致初中		公費		121.478996	31.2416039	\N
41	上海市長寧區北二幼兒園	6	園長：楊劍華	上海市長寧區新涇三村45號	1	http://3101050167.age06.com/310105/526/	“我閱讀我快樂”故事會活動03早教活動	"1.新涇二村；2.新涇三村；3.北漁路:82弄、115-135弄 ；4.北虹路:1-1185號；5.哈密路:273號、277號、398弄、342號、482弄；6.劍河路（雙）:404-414弄    泉口路128弄；7.天山西路（單）:1-95號     天山西路:199-211弄"\t\r\n			幼管費：225元/；外籍：1300月/月；伙食費：9元/人/天 ；點心費：4元/人/天		121.379997	31.2199993	\N
43	上海市長寧區基金會幼兒園	6	園長：許梅；全園在編教職工49名，其中專任教師38人，幼兒園進階教師18人，占教師總數的47.4%，一級教師20人，占教師總數的52.6%；教師中碩士研究生1人、本科生33人、大專生4人（2人在讀本科），大專學歷及格率為100%。幼兒園設園長1人，黨支部書記（兼副園長）1人，其中1人國中進階職稱。幼兒園還配備了專職保健老師4人，營養員2人，保育員3人，出納、財產保管員各1人。\r\n	上海市長寧區松江路685弄3號	1	http://3101050178.age06.com/310105/534/	美術節微標評選活動\r\n	"1.淞虹路:650弄、685弄；2.甘溪路:368弄； 3.泉口路:225弄 ；4.協和路:68弄；5.福泉路:255弄、385弄、435弄、495弄；6.仙霞西路:700弄、715弄、885弄、888弄"\t\r\n			幼管費：225元/月；外籍：1300月/月；伙食費：9元/人/天 ；點心費：4元/人/天		121.389999	31.2099991	\N
47	上海市長寧區貝爾幼稚園	6		上海市長寧區虹橋路2192號	1	http://www.beyzy.com/	“愛心義賣”活動；教研活動；親子活動； 雙語活動\r\n	全年招生。1.5-6歲的中、外籍小朋友（不限戶籍，國籍，隨時入園）\t\r\n			雙語班：4200元/月/人  國標班：6000元/月/人    伙食費：9元/月/人      點心費：4元/月/人     校車接送：600元/月/人   半日班（中籍）：2100元/月/人                半日班（外籍）：3000元/月/人		121.389999	31.2000008	\N
40	上海市長寧區紫一幼兒園	6	園長：陶曉艷           教職工26名。\r\n幼兒園有一支經驗豐富的教職工隊伍。100℅的教師具有大專學歷，進階職稱的老師占90℅	上海市長寧區婁山關路462號	1	http://3101050152.age06.com/310105/512/		1.天山二村:1-150號                  2.天山路(單):751-989號\r\n3.婁山關路:425-480弄                4.仙霞路:133-297弄\r\n5.紫雲西路:28弄、50弄、89弄          6.茅台路:200弄1-17號\r\n7.古北路:439-503號、555弄、585弄   8.興義路:48號、85-99號\r\n9.萬山路:1-60號                     10.雲霧山路\r\n11.遵義路(單):429-585號          \r\n12.玉屏南路(單):309號、329號、345-499弄\r\n玉屏南路(雙):340-490弄			幼管費：175元/月                        伙食費：9元/人/天               點心費：4元/人/天		121.410004	31.2099991	\N
44	上海市長寧區威寧路幼兒園	6	園長：劉穎                  幼兒園共有教職工22名，其中教師15人，大專學歷100%，本科學歷9人，占60%，進階教師9名，占60%。	茅台路715弄18號	1	http://3101050173.age06.com/310105/529/	大班中日幼兒混班戶外活動  經常性運動活動  	1.茅台路:575-830弄\r\n2.安龍路:698-960弄\r\n3.仙霞路(單號):577-737弄\r\n4.威寧路:276弄、358弄\r\n5.新漁東路:200號、289-358弄\r\n6.水城路(單號):445-511弄的適齡兒童			幼管費：175元/月；外籍：1300月/月；伙食費：9元/人/天；點心費：4元/人/天		121.392372	31.2147388	\N
46	上海市長寧區新實驗幼兒園	6	園長：周劍	雙流路380號	1	http://3101050305.age06.com/310105/14972/		電腦派位\r\n登記範圍：\r\n幼兒戶籍在威寧路511弄、天山路202弄的適齡兒童			幼管費：175元/月；伙食費：9元/人/天；點心費：4元/人/天		121.387779	31.2243805	\N
51	上海市長寧區愚園路第一幼兒園(遵義路分園)	4	園長：高雯彬            擁有一支專業素養較高、充滿朝氣的教師隊伍，他們在教學上敢於突破創新，致力於教育敘事的研究，部分青年教師已經脫穎而出，先後在近幾年的“長教杯”、“希望杯”、“育英杯”、“黃浦杯”、“創新運用大擂台”等比賽中屢屢獲獎。	遵義路800弄28號	1	http://3101050096.age06.com/310105/457/		1.長寧路:1488-1898 弄、1447-1661 弄\r\n2.遵義路:757 弄、797 弄、800 弄、820 號\r\n3.中山西路:340-380 號 \r\n4.婁山關路:999 弄\r\n5.萬航渡路:2505 弄 萬航渡路（雙）:2486-2590 號 			幼管費：175元/月；外籍：1300月/月；伙食費：9元/人/天；點心費：4元/人/天		121.416267	31.222065	\N
53	上海市黃浦區梅溪小學	3	校長姓名：吳建國\r\n教職工55名，其中小學進階教師15人。	永寧街20號	2	http://www.meixi.hpe.cn/	浦江游、伙伴情、放飛蝴蝶，放飛心願、學先烈，祭英雄，促成長、為愛找一個支點。	大興、喬家柵、小西門、龍門村、牌樓、陸興、曹家街、學宮、也是園			公費		121.495773	31.2214012	\N
54	上海市黃浦區光明小學	3	光明小學師資力量強，教師學歷100%合格（大專、大本學歷達到85%），小學進階教師達90%，一批充滿活力，具有奉獻、創新精神的中青年教師活躍在教學第最前線。	傅家街40號（傅家街盛家街）	2	http://gmxx.hpe.cn/	搞腦子，金點子，拿牌子、“小小航太迷”遇上“飛天大英雄”	果育、侯家、丹馬、學院、廣福、寶帶、古城			公費		121.500084	31.2293987	\N
55	上海市黃浦區董家渡路第二小學	3	在職教師59人，其中29人獲小學進階職稱，11人已達到學本科、大專學歷26人正在攻讀大專學歷，師資質量穩步上升。	西姚家弄48號	2	http://school.ci123.com/firms/84552/infos-show		中華、西姚	尚文國中		公費		121.50293	31.2283401	\N
56	上海市黃浦區淮海中路小學	3	校長姓名：張敏	淡水路93號（近太倉路）	2	http://www.huaixiao.lwedu.sh.cn/	我是安全小護士、我設計、我創造、我快樂、學中華古詩文，做文明號少年和小樹一起成長	孝和、西成、瑞興、新天地			公費		121.47921	31.2269897	\N
52	上海市黃浦區第一中心小學	3	校長姓名：張燁\r\n學校專職老師人數73人，其中中級以上老師比例79%，現有國中教師7人，區學科帶頭人以及區、校級骨干教師16人，中國共產黨黨員22人。	董家渡路165號（近白渡路）	2	http://yzx.hpe.sh.cn/	體育類別 科技類別 藝術類別 游戲足間，晨間飛揚、快樂暑假DV游、童心向黨、書香滿校園、奇妙深海之旅、同心向領巾	白渡、新碼、多稼、陽光、桑園、王碼、萬裕	上海市儲能國中		公費		121.510002	31.2299995	\N
57	上海市長寧區金鍾路幼兒園	6	園長：畢一軍	上海市長寧區金鍾路333弄87號（近福泉路）	1	http://3101050176.age06.com/310105/532/	經常性展開室內運動研討活動	1.天山西路:450弄；2.金鍾路:333弄、428弄；3.平塘路:100弄、155弄、165弄、175弄、185弄；4.淞虹路:128弄；5.西淘濱路:28弄；6.北翟路:980弄；7.雙涇村、努力村、北翟地區（劍河路以西）；8.清池路:102號、200弄；			幼管費：175元/月；外籍：1300月/月；伙食費：9元/人/天 ；點心費：4元/人/天；		121.369286	31.2249985	\N
35	上海市長寧區古一幼兒園	6	園長：王玉琴  ；擁有一支以青年為主的教師隊伍，教師100%達到大專學歷，其中75%的教師達到大學本科學歷。\r\n	上海市長寧區天山路700弄4號	1	http://3101050162.age06.com/310105/521/		"1.芙蓉江路:177 弄、555 弄；2.錦屏路 ；3.古北路（單）:69-373 弄 ；4.古北路:108弄、124 號、136 弄 古北路（雙）:368-452 號；5.天山四村；6.天山五村:1-147 號；7.茅台路（雙）:216-382 號 ；8. 天山支路 ； 9. 天山路:651-681 號、600-680 弄 天山路；（雙）：700-938 弄；10.玉屏南路（單）:505-731 弄 玉屏南路（雙）:496-560 弄 ；11.婁山關路（單）:815-969 弄 婁山關路（雙）:758-888 號 "\t\r\n			幼管費：175元/月 ； 伙食費：9元/人/天 ；點心費：4元/人/天		121.410004	31.2199993	\N
58	上海市長寧區南新幼兒園	6	園長：李玲君	上海市長寧區新漁東路630號	1	http://3101050181.age06.com/310105/536/	南新幼兒園課題群組活動；03早教活動（03散居兒童早教指導宣傳活動、03雙休日親子班活動、03貝貝班活動、入托經驗活動）；主旨活動、數活動、藝術活動、生活經驗活動、等）	1.天山路:177 弄、198 號、209 弄、288 弄；2.雙流路:54 弄、188 弄；3.威寧路:291 弄、339 弄；4.新漁東路:455 弄、456 弄、550 弄；5.青溪路:555 弄、601 弄；6.仙霞路:1118 弄、1225 弄、1316 弄、1388 弄；7.淮陰路:575 弄、599 弄；8.茅台路:900 弄；			幼管費：225元/月；外籍：1300元/月；伙食費：9元/人/天；點心費：4元/人/天；		121.387947	31.2193241	\N
60	上海市長寧區虹橋路第二幼兒園	6	園長：車佳平	上海市長寧區虹橋路996弄26號	1	http://3101050156.age06.com/310105/516/	03早教活動	1.虹橋路（雙）:996-1038 弄 虹橋路;1060 號、1168 弄 虹橋路（單）:953-971 弄；2.中山西路:1221-1251 號 中山西路:1265-1432 弄；			幼管費：225元/月；外籍：1300元/月；伙食費：9元/人/天；點心費：4元/人/天；		121.426376	31.2008476	\N
76	上海市長寧區長寧路小學	6	校長：陸勤；學校的教師也正透過不斷的努力，提昇自己教育教學的素養。\r\n	上海市長寧區長寧路1600弄15號	2			萬航渡路：2032 弄-2616 弄 ；長寧路：1120 弄、1135-2197 ；中山西路：85-187（單號）、189 弄、340-450（雙號）、483 號 ；遵義路：555-820 號 ；玉屏南路：110-476（雙號）； 天山三村：全部 ；雲霧山路：2-27 號 \t\r\n	新古北國中；姚連生國中；長寧國中；婁山國中。		外籍：1300元/人/學期；課外教育活動費：100元/人/學期；校服費：不超過300/人/套；餐費：不超過12元/人/餐		121.410004	31.2199993	\N
34	上海市長寧區海貝幼兒園	6	園長：盧碧瀅   現擁有52名專職教師，其中本科學歷35人占74.5%；本科在讀11人；5年以上教齡教師39名，其中區級骨干教師12人，校級骨干教師15人。                 擁有一支團結向上、充滿活力的教工隊伍。其中有全國優秀教師，多名幼兒園進階教師，區級骨干教師、區級“園丁獎”稱號的教師。	總園：上海市長寧區定西路710弄37號                        分園：法華鎮路751弄45號	1	http://haibei.age06.com/310105/517/	“我HAPPY，我最棒”系列活動;“幼兒結構游戲”活動	1.番禺路（單）:1號-207弄、\r\n209弄1號-23支弄（弄內單號）\r\n番禺路（雙）:2-220弄、\r\n222弄1-51號（弄內單號）\r\n2.幸福路:211-441弄\r\n3.平武路（單）:7-131弄\r\n平武路（雙）:8-168弄\r\n4.定西路（單）:591-825號\r\n定西路（雙）：710-798號\r\n5.新華路（雙）:506-728號\r\n6.法華鎮路（單）:633-915號\r\n法華鎮路（雙）:660-930號\r\n7.種德橋2號\r\n8.延安西路（雙）:1152-1696號（1350弄除外）\r\n9.凱旋路（雙）:1010-1068號\r\n10.楊宅路（單）:1-97號\r\n楊宅路（雙）:2-86號\r\n11.華山路1220弄（集體戶口除外）			幼管費：225元/月;外籍：1300月/月;伙食費：9元/人/天;點心費：4元/人/天		121.43	31.2099991	\N
63	上海市長寧區長華幼兒園	6	園長：陸慧琴；教工21人；專任教師11人，100%具有大專學歷、85%具有本科學歷；專任教師中幼兒園進階教師有10人，占91%。	上海市長寧區長寧路491弄14號	1	http://changhua.age06.com/310105/514/	上海教育出版社與幼兒學互動活動	1.長寧路:57-518弄\r\n2.愚園路:1210弄、1240弄\r\n3.長寧支路\r\n4.萬航渡路1424弄及以前\r\n5.江蘇北路\r\n6.華陽路\r\n7.江蘇路（雙）：46-82弄\r\n8.安西路:23弄\r\n9.萬航渡路後路:77弄、85號、87號			幼管費：175元/月;伙食費：9元/人/天; 點心費：4元/人/天		121.433517	31.2277851	\N
50	上海市長寧區新華路幼兒園	6	園長：蘇艷紅	上海市長寧區新華路294弄11號	1	http://3101050149.age06.com/310105/509/		"1.番禺路（單）:211號及以後、209 弄（弄內雙號） 番禺路（雙）:224弄及以後、222弄（弄內雙號） ；2.法華鎮路（單）:1-631 號 法華鎮路（雙）:2-632 號；3.新華路（單）:1-483 號 新華路（雙）:2-468 號；4.幸福路（單）:1-139 號 幸福路:195 號 幸福路（雙）:2-200 號；5.華山路:1389 弄、1461 弄、1520 號及以後；6.定西路（雙）:2-708 號；7.淮海中路:1950 弄、1978 號及以後；8.興國路（雙）； 9.香花橋路 ；10.淮海西路（雙）；11.雲陽路；12.泰安路； 13.湖南路"\t\r\n			幼管費：175元/月；外籍：1300月/月；伙食費：9元/人/天 ；點心費：4元/人/天		121.43	31.2099991	\N
70	上海市長寧區虹古路第三幼兒園	6	園長：張薇；全院在編人員21人。擁有一支師德良好，整體結構比較合理的師資隊伍。在現有的17位教師中，全部具有大專學歷，其中12位教師具有本科學歷，占70%，一名研究生在讀。	上海市長寧區仙霞路700弄43號	1	http://3101050166.age06.com/310105/525/	故事周活動	1.仙霞路: 1001 弄 仙霞路（雙）: 620-1088 弄                             \r\n2.清溪路: 770 弄 25 號             \r\n 3.北虹路: 77 弄、555 弄、579 弄 \r\n4.虹古路:380-829 弄                 \r\n5.安龍路:465 弄                       \r\n6.威寧路:8 弄、123 弄 			幼管費：175元/月     外籍：1300元/月 ；伙食費：9元/人/天 ；點心費：4元/人/天		121.392784	31.2110004	\N
59	上海市長寧區愚園路第五幼兒園	6	園長：徐芸；教師隊伍學歷全部達到大專學歷。其中80%教師已達到本科學歷。教師的年齡階層均衡，且具有一定的教學經驗。60%教師持有幼兒園進階教師職稱。	上海市長寧區愚園路865弄4號	1	http://3101050146.age06.com/310105/506/	“科技大篷車”進校園活動	1、愚園路：(雙)684—1088弄、1112弄、1136弄(單)669弄—1249弄；2、江蘇路：(雙)114—320弄（單）5號—501號；3、武定西路：（單）1201-1371弄、1375號；4、鎮寧路：（單）111號、233弄—545弄；5、延安西路：（雙）548弄—746弄；6、宣化路：（雙）42—72弄、248弄；7、東諸安濱路：55弄—231弄；			幼管費：175元/月；外籍：1300元/月；伙食費：9元/人/天；點心費：4元/人/天；		121.440002	31.2299995	\N
62	上海市長寧區兆豐幼兒園	6	園長：鄭衛權	上海市長寧區長寧路712弄151號	1	http://3101050143.age06.com/310105/503/	早期閱讀特色活動；公園野趣活動；特色專業活動室   	1.長寧路（雙）:582-1318 弄        \r\n2.凱旋路:10 弄、14 號、88-138 號      \r\n3.匯川路:300 弄、400 弄  \r\n4.中山西路:85 弄、189 弄            \r\n 5.萬航渡路: 1425 號                  \r\n萬航渡路（單）:1455 號-1589 號                        \r\n萬航渡路（雙）:1450-2088 弄 	長寧路小學;江五小學;		幼管費：225元/月； 外籍：1300元/月；伙食牛奶費：13元/人/天		121.428741	31.2284489	\N
66	上海市長寧區愚一幼兒園	6	園長：張蕙	總院：上海市長寧區愚園路1280弄18號;分院：上海市長寧區安化路20號       	1	http://3101050144.age06.com/310105/504/		1.匯川路:10 弄、88 弄                \r\n2.長寧路:833 弄、969 號、1027 弄、1033 弄、 1277 弄                         \r\n3.安西路:10-380 號  \r\n4.定西路:1277 號、1279 號、1507 號、1564 號                             \r\n 5.宣化路:268 弄                       \r\n6.愚園路:1264-1396 號、1277-1423 弄 \r\n7.安化路:394 號、396 號、400 號、470 號 			幼管費：700元/月     外籍：1300元/月; 伙食費：9元/人/天 ;點心費：4元/人/天		121.43132	31.2256699	\N
67	上海市長寧區新劍幼兒園	6	園長：姚紅梅；共計60名教職員公，其中教師34人。教師的人員結構合理，教師持證就職，100%的教師參加學歷教育訓練和職務教育訓練，其中大學本科及本科在讀的教師達81%，大專畢業達19%，教師學歷階層較高。	上海市長寧區劍河路459號	1	http://3101050177.age06.com/310105/533/		1.平塘路:456 弄                       \r\n2.甘溪路:100 弄、205 號、207 號          \r\n3.劍河路:599 弄、602 弄、688 弄、711 弄                                   \r\n 4.哈密路:500 弄                      \r\n5.泉口路:109 弄、185 弄 \r\n6.仙霞路:1281 弄、1331 弄             \r\n7.仙霞西路:77 弄、300 弄、500 弄、501 弄 621 弄、630 弄、635 弄            \r\n8.淞虹路:715 弄、735 弄               \r\n9.福泉路:258 弄			幼管費：175元/月     外籍：1300元/月; 伙食費：9元/人/天 ; 點心費：4元/人/天		121.374825	31.2173786	\N
68	上海市長寧區安順路幼兒園	6	園長：宗艷 ;工會主席：劉晨  ;保教主任：胥夢超	上海市長寧區安順路193號	1	http://3101050155.age06.com/310105/515/		1.長順路                             \r\n2.安順路                           \r\n 3.虹橋路:885 弄、977 弄              \r\n 4.新華路（單）:519 號-699 弄 新華路:755 弄 \r\n5.楊宅路:181 弄、266 弄             \r\n6.中山西路（單）:945-1039 弄         \r\n7.延安西路（雙）:1740-1930 弄        \r\n8.凱旋路:1188 號、1222 弄、1500 弄   \r\n9.定西路（單）:399-439 弄			幼管費：175元/月     外籍：1300元/月;伙食費：9元/人/天； 點心費：4元/人/天		121.42691	31.2085838	\N
69	上海市長寧區虹橋幼兒園	6	園長：胡巨集	上海市長寧區張虹路92號	1	http://3101050193.age06.com/310105/541/		1. 古北聖美邸（宋園路 69 弄）        \r\n2. 張虹路 90 弄                     \r\n3. 虹橋城市花園（黃金城道 99 弄）    \r\n4. 古北中央花園（伊犁南路 500 號）  \r\n 5. 古北國際廣場（富貴東道 229 弄）   \r\n6. 伊犁路:110-146 弄 \r\n7.潘家塔（1-40 號）                \r\n 8.姚虹路 619 弄                     \r\n9.虹橋路（單）:1017-1167 弄        \r\n10.古北嘉年華庭（黃金城道 258/259 號） \r\n11.中山西路 1030 弄                \r\n12.宋園路:28-62 弄			幼管費：225元/月； 外籍：1300元/月; 伙食費：9元/人/天 ；點心費：4元/人/天		121.418983	31.1985912	\N
61	上海市長寧區民辦東展幼兒園	6	園長：范怡；首席顧問：趙赫；依據公司“投資機制、投資人才，報務社會、爭創品牌”的投資理念，幼兒園師資隊伍結構合理，擁有一批在市、區有一定影響力的、高素質的中青年教師隊伍，目前有市、區級骨干教師7人。教師們富有愛心、服務意識強，專業水准高。幾年來，教師們在各級各類別業務專業比賽中有2項24人次獲全國獎項，7項10人獲上海市獎項。	上海市長寧區安龍路828號	1	http://www.dongzhan-dzy.com.cn/	戶外幼兒混齡大活動；活動區活動課程；幼兒生活課程——‘我會做’幼兒音樂；園本化的皮亞傑幼兒思維課程；	2015招生物件：我園招收身體健康（無慢性傳染病）、智力標準、可標準參加集體活動的適齡兒童。實際年齡段：2012 年 9 月 1 日至 2013 年 8 月 31 日；2011 年 9 月 1 日至 2012 年 8 月 31 日（僅收部分插班生）。暫無實際地段訊息。			幼管費：3500元/月；外籍：4300元/月；伙食費：11元/人/天；點心費：5元/人/天；		121.394226	31.2145519	\N
64	上海市長寧區長三幼兒園	6	園長：徐英	上海市長寧區武夷路709弄28號	1	http://3101050161.age06.com/310105/520/		1.武夷路（單）:411-727 號 武夷路（雙）:416-800 號                    \r\n2.延安西路（單）:1431-1667 弄        \r\n3.長寧路:1135 弄                     \r\n4.定西路:1211 弄、1235 弄、1327 號    \r\n5.天山路（雙）:1650-1820 弄           \r\n6.玉屏南路:1-227 號                   \r\n7.凱旋路:750 弄 \r\n8.中山西路（單）:333-753 號 中山西路：424 弄、430 號、440 號、450 號         \r\n9.安化路（單）:395-535 號           \r\n10.昭化路（單）:501-615 號 昭化路（雙）:488-518 弄                    \r\n11.遵義路:友誼新村 1-7號、390-412 弄、534弄、 690 號、700 號、720 號、740 號、780 弄                             \r\n12.天山三村:1-49 號 			幼管費：175元/月; 伙食費：9元/人/天;點心費：4元/人/天		121.423096	31.2200413	\N
65	上海市長寧區虹古路幼兒園	6	園長：黃瑛；全院在編人員21人。現有的17位教師中，全部具有大專學歷，其中12位教師具有本科學歷，占70%，一名研究生在讀。	上海市長寧區虹古路379號	1	http://3101050165.age06.com/310105/524/		1.虹古路（單）:11-377 弄              \r\n2.水城路:2-79 號                     \r\n3.虹橋路:1704 號-1980 弄              \r\n4.虹許路:815 弄-1109 弄  \r\n5.虹梅路:1918-3918 弄                \r\n6.延安西路:2633 號—2932 弄             \r\n7.水城南路:25 號-348 弄              \r\n 8.榮華西道:19-128 號 			幼管費：175元/月；外籍：1300元/月;伙食費：9元/人/天; 點心費：4元/人/天		121.395538	31.2087688	\N
77	上海市長寧區古北路小學	6	校長：周明星；教職工53人，其中國中進階教師2人，小學進階教師25人，大學本科學歷28人占在崗教師65.1%，大專14人，2人完成了研究生課程研讀，在職在崗教師學歷合格率達100%。\r\n	上海市長寧區古北路211弄24號	2	http://www.gubeischool.com/index.html	“機器人”、“咕咕兒童詩社”、“乒乓球”“兒童畫”“生活德育”“民俗與禮儀”。\r\n	天山路：680 弄、700 弄、750 弄-840 弄 （雙號）；古北路：4-186 號（雙號）、8 弄、62 弄、69 弄、76 弄、108 弄、181 弄、124 弄、136 弄、211 弄-250 弄、371 弄-373 弄； 婁山關路：811 弄-827 號（單號）、850 弄、969 弄、999 弄； 雲霧山路：221 弄、551 弄 ；玉屏南路：496 弄、498 弄、510 弄-618 弄、537-731 弄； 天山四村全部 ；錦屏路全部； 天山支路全部 ；芙蓉江路 555 弄（新天地河濱花園） 	新古北國中；姚連生國中；長寧國中；婁山國中。		外籍：1300元/人/學期；課外教育活動費：100元/人/學期；校服費：不超過300/人/套；餐費：不超過12元/人/餐		121.401215	31.2136765	\N
78	長寧區玉屏南路小學	6	校長：樂漣；在崗教職員公47名，其中教師42名。	上海市長寧路玉屏南路371號	2	http://wl1977.30edu.com/	環保群組、機械及其人族、科普繪畫群組、攝影群組、玉屏詩社等。	遵義路：390 弄-412 弄、435 弄、533 號、543 號； 友誼新村：1-7 號 ；玉屏南路：1-207 號（單號）、41 弄、113 弄、345 弄、375 號、309 號、 329 號、377 號、379 號； 天山路：1726 弄 1-11 號、938 弄、1878 弄-1922 弄 ；中山西路：640 號（雙號）-652 弄 3 號、669 弄-753 號 ；婁山關路：764 弄、810 弄 武夷路：651-741（單號）、656-790（雙號） \t\r\n	新古北國中；姚連生國中；長寧國中；婁山國中。		外籍：1300元/人/學期；課外教育活動費：100元/人/學期；校服費：不超過300/人/套；餐費：不超過12元/人/餐		121.406784	31.2130165	\N
75	上海市長寧區安順路小學	6	校長：陶永儀；全校有104名教職工，群組成了一支有責任心、和諧、進取的團隊。其中小學進階教師67名，小學一級教師26名，教職工中共產黨員21名，共青團員8名。\r\n	上海市長寧區安順路215號	2	http://www.aslxx.edu.sh.cn/info/FRAME_INDEX.asp?info_class_id=182&height=768&width=1024	《小籃球》；《航太知識》；《DV製作》等拓展課程。\r\n	虹橋路：885 號-1392 號； 延安西路：1740 弄-1930 弄（雙號）； 宋園路：1-108 ；伊犁路：2 號-110 弄、134 弄、146 弄、190 弄； 黃金城道：99 弄、潘家塔、姚虹路虹四村 ；中山西路：934-1432（雙號）、945-1251（單號）； 中山西路何家角全部；中山西路中華新村全部；中山西路長順路全部 安順路：134-358（雙號）；158-389 號（單號） 紡大教工宿捨（延安西路 1882 號；延安西路 1930 弄；楊宅路 181 弄）； 凱旋路：1383 號  \t\r\n	滬定國中；長寧國中；婁山國中；		外籍：1300元/人/學期；課外教育活動費：100元/人/學期；校服費：不超過300/人/套；餐費：不超過12元/人/餐		121.416435	31.2004471	\N
79	上海市長寧區新世紀小學	6	校長：楊毅蓉；擁有一支資力深，職稱高，教學經驗豐富，老中青結構優良的師資隊伍。現有教師30名，具有國中進階教師職稱4名，小學進階教師職稱14名。教師中曾榮獲全國及市級以上“園丁獎”稱號有12人次，榮獲區級以上“園丁獎”稱號有30人次	上海市長寧區新鍋爐374弄2號	2	http://www.mbxsjxx.com/	洋樂器；合唱隊；兒童畫創作等。；訊息技術、國防視野、外教閱讀、機器人、模型製作、創意設計、紙籐花藝、彩陶、管樂吹奏、芭蕾舞、工筆畫、書法、民間工藝、小足球等近30門課。\r\n	自主招生			學費：15000元/人/學期；課外教育活動費：100元/人/學期；校服：不超過400元/人/套；餐費：14元/人/餐；校車費：890元/人/月。		121.422203	31.2181225	\N
\.


--
-- Data for Name: school_feature; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY school_feature (school_id, feature_id) FROM stdin;
75	3
76	3
76	6
76	1
77	3
77	1
78	5
79	6
79	1
79	2
79	4
13	0
14	0
16	0
19	0
21	0
22	0
28	6
29	6
29	3
30	2
31	6
31	3
33	2
35	2
36	2
37	4
41	2
42	4
42	2
43	2
44	0
45	0
46	0
47	2
47	3
48	0
49	4
50	2
51	0
57	2
59	2
60	2
61	3
\.


--
-- Name: school_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('school_id_seq', 79, true);


--
-- Data for Name: schoolimage; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY schoolimage (id, school_id, file) FROM stdin;
\.


--
-- Name: schoolimage_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('schoolimage_id_seq', 31, true);


--
-- Data for Name: schooltype; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY schooltype (id, name) FROM stdin;
1	幼兒園
2	小學
3	初中
4	高中
5	中等職業學校
6	大專
7	大學
\.


--
-- Name: schooltype_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('schooltype_id_seq', 7, true);


--
-- Data for Name: terminal; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY terminal (id, account_id, type, code) FROM stdin;
\.


--
-- Name: terminal_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('terminal_id_seq', 1, false);


--
-- Data for Name: test; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY test ("user", tt) FROM stdin;
\.


--
-- Name: account_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY account
    ADD CONSTRAINT account_pkey PRIMARY KEY (id);


--
-- Name: advert_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY advert
    ADD CONSTRAINT advert_pkey PRIMARY KEY (id);


--
-- Name: agespan_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY agespan
    ADD CONSTRAINT agespan_pkey PRIMARY KEY (id);


--
-- Name: area_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY area
    ADD CONSTRAINT area_pkey PRIMARY KEY (id);


--
-- Name: bulletin_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY bulletin
    ADD CONSTRAINT bulletin_pkey PRIMARY KEY (id);


--
-- Name: bulletinimage_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY bulletinimage
    ADD CONSTRAINT bulletinimage_pkey PRIMARY KEY (id);


--
-- Name: feature_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY feature
    ADD CONSTRAINT feature_pkey PRIMARY KEY (id);


--
-- Name: feetype_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY feetype
    ADD CONSTRAINT feetype_pkey PRIMARY KEY (id);


--
-- Name: institution_feature_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY institution_feature
    ADD CONSTRAINT institution_feature_pkey PRIMARY KEY (institution_id, feature_id);


--
-- Name: institution_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY institution
    ADD CONSTRAINT institution_pkey PRIMARY KEY (id);


--
-- Name: institutionimage_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY institutionimage
    ADD CONSTRAINT institutionimage_pkey PRIMARY KEY (id);


--
-- Name: school_feature_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY school_feature
    ADD CONSTRAINT school_feature_pkey PRIMARY KEY (school_id, feature_id);


--
-- Name: school_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY school
    ADD CONSTRAINT school_pkey PRIMARY KEY (id);


--
-- Name: schoolimage_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY schoolimage
    ADD CONSTRAINT schoolimage_pkey PRIMARY KEY (id);


--
-- Name: schooltype_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY schooltype
    ADD CONSTRAINT schooltype_pkey PRIMARY KEY (id);


--
-- Name: terminal_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY terminal
    ADD CONSTRAINT terminal_pkey PRIMARY KEY (id);


--
-- Name: test_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY test
    ADD CONSTRAINT test_pkey PRIMARY KEY ("user");


--
-- Name: institution_agespan_id_idx; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX institution_agespan_id_idx ON institution USING btree (agespan_id);


--
-- Name: institution_area_id_idx; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX institution_area_id_idx ON institution USING btree (area_id);


--
-- Name: institution_feature_feature_id_idx; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX institution_feature_feature_id_idx ON institution_feature USING btree (feature_id);


--
-- Name: institution_feature_id_idx; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX institution_feature_id_idx ON institution USING btree (feature_id);


--
-- Name: institution_feature_institution_id_idx; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX institution_feature_institution_id_idx ON institution_feature USING btree (institution_id);


--
-- Name: institution_feetype_id_idx; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX institution_feetype_id_idx ON institution USING btree (feetype_id);


--
-- Name: institutionimage_institution_id_idx; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX institutionimage_institution_id_idx ON institutionimage USING btree (institution_id);


--
-- Name: school_area_id_idx; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX school_area_id_idx ON school USING btree (area_id);


--
-- Name: school_feature_feature_id_idx; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX school_feature_feature_id_idx ON school_feature USING btree (feature_id);


--
-- Name: school_feature_id_idx; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX school_feature_id_idx ON school USING btree (feature_id);


--
-- Name: school_feature_school_id_idx; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX school_feature_school_id_idx ON school_feature USING btree (school_id);


--
-- Name: school_schooltype_id_idx; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX school_schooltype_id_idx ON school USING btree (schooltype_id);


--
-- Name: schoolimage_school_id_idx; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX schoolimage_school_id_idx ON schoolimage USING btree (school_id);


--
-- Name: terminal_account_id_idx; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX terminal_account_id_idx ON terminal USING btree (account_id);


--
-- Name: bulletinimage_bulletin_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY bulletinimage
    ADD CONSTRAINT bulletinimage_bulletin_id_fkey FOREIGN KEY (bulletin_id) REFERENCES bulletin(id);


--
-- Name: institution_feature_ibfk_1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY institution_feature
    ADD CONSTRAINT institution_feature_ibfk_1 FOREIGN KEY (institution_id) REFERENCES institution(id) ON UPDATE CASCADE ON DELETE CASCADE DEFERRABLE INITIALLY DEFERRED;


--
-- Name: institution_feature_ibfk_2; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY institution_feature
    ADD CONSTRAINT institution_feature_ibfk_2 FOREIGN KEY (feature_id) REFERENCES feature(id) ON UPDATE CASCADE DEFERRABLE INITIALLY DEFERRED;


--
-- Name: institution_ibfk_2; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY institution
    ADD CONSTRAINT institution_ibfk_2 FOREIGN KEY (feetype_id) REFERENCES feetype(id) ON UPDATE CASCADE DEFERRABLE INITIALLY DEFERRED;


--
-- Name: institution_ibfk_3; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY institution
    ADD CONSTRAINT institution_ibfk_3 FOREIGN KEY (area_id) REFERENCES area(id) ON UPDATE CASCADE DEFERRABLE INITIALLY DEFERRED;


--
-- Name: institution_ibfk_4; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY institution
    ADD CONSTRAINT institution_ibfk_4 FOREIGN KEY (agespan_id) REFERENCES agespan(id) ON UPDATE CASCADE DEFERRABLE INITIALLY DEFERRED;


--
-- Name: institution_ibfk_5; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY institution
    ADD CONSTRAINT institution_ibfk_5 FOREIGN KEY (feature_id) REFERENCES feature(id) ON UPDATE CASCADE DEFERRABLE INITIALLY DEFERRED;


--
-- Name: institutionimage_ibfk_1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY institutionimage
    ADD CONSTRAINT institutionimage_ibfk_1 FOREIGN KEY (institution_id) REFERENCES institution(id) ON UPDATE CASCADE ON DELETE CASCADE DEFERRABLE INITIALLY DEFERRED;


--
-- Name: school_feature_feature_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY school_feature
    ADD CONSTRAINT school_feature_feature_id_fkey FOREIGN KEY (feature_id) REFERENCES feature(id) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- Name: school_feature_ibfk_1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY school_feature
    ADD CONSTRAINT school_feature_ibfk_1 FOREIGN KEY (school_id) REFERENCES school(id) ON UPDATE CASCADE ON DELETE CASCADE DEFERRABLE INITIALLY DEFERRED;


--
-- Name: school_ibfk_1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY school
    ADD CONSTRAINT school_ibfk_1 FOREIGN KEY (schooltype_id) REFERENCES schooltype(id) ON UPDATE CASCADE DEFERRABLE INITIALLY DEFERRED;


--
-- Name: school_ibfk_2; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY school
    ADD CONSTRAINT school_ibfk_2 FOREIGN KEY (area_id) REFERENCES area(id) ON UPDATE CASCADE DEFERRABLE INITIALLY DEFERRED;


--
-- Name: school_ibfk_3; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY school
    ADD CONSTRAINT school_ibfk_3 FOREIGN KEY (feature_id) REFERENCES feature(id) ON UPDATE CASCADE DEFERRABLE INITIALLY DEFERRED;


--
-- Name: schoolimage_ibfk_1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY schoolimage
    ADD CONSTRAINT schoolimage_ibfk_1 FOREIGN KEY (school_id) REFERENCES school(id) ON UPDATE CASCADE ON DELETE CASCADE DEFERRABLE INITIALLY DEFERRED;


--
-- Name: terminal_ibfk_1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY terminal
    ADD CONSTRAINT terminal_ibfk_1 FOREIGN KEY (account_id) REFERENCES account(id) ON UPDATE CASCADE ON DELETE CASCADE DEFERRABLE INITIALLY DEFERRED;


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

