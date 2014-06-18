__author__ = 'sjames'
__copyright__ = 'Copyright (C) 2014 Steven James'
__license__ = "Public Domain"
__version__ = "0.1"
__email__ = "sjames@ctiengr.com"
__status__ = "Beta"

NAME_FIELD = "ggt_textbox(14)"
EMAIL_FIELD = "ggt_textbox(50)"

class AddressEntry:
    def __init__(self, name="", email=""):
        self.address_entry_data = { #the following data taken from a sample post made in a browser
            "addrbook_entryWebchange":"",
            "action":"submitbtn",
            "ordinate":"501",
            "addrentry_profid(0)":",1,0,1,7,1,0,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,1,",
            "addrentry_hyperlinkdestids":"",
            "addrentry_ftp_hyperlinkhid_list":"",
            "addrentry_smb_hyperlinkhid_list":"",
            "addrentry_WarningMsg":"0,",
            "addrentry_WarningNum":"0,",
            "addrentry_AlreadyName":"",
            "addrentry_AlreadyDetailid":"0,",
            "addrentry_ftp_hyperlink_sel_hidden":"6002,",
            "addrentry_smb_hyperlink_sel_hidden":"6002,",
            "addrentry_tabno_hidden":"0,",
            "ggt_select(7)":"1",
            "ggt_textbox(11)":"",
            "ggt_textbox(14)":"", #name
            "ggt_textbox(17)":"",
            "ggt_select(23)":"1",
            "ggt_hidden(32)":"0",
            "ggt_select(49)":"",
            "ggt_textbox(50)":"sjames@ctiengr.com", #email address
            "ggt_select(51)":"0",
            "ggt_select(52)":"2",
            "ggt_select(53)":"1",
            "ggt_checkbox(54)":"1", #default
            "ggt_select(65)":"0",
            "ggt_textbox(69)":"",
            "ggt_select(67)":"0",
            "ggt_select(68)":"0",
            "ggt_select(81)":"0",
            "ggt_textbox(82)":"",
            "ggt_select(84)":"0",
            "ggt_select(86)":"0",
            "ggt_textbox(87)":"",
            "ggt_textbox(90)":"",
            "ggt_select(92)":"0",
            "ggt_select(113)":"0",
            "ggt_textbox(114)":"",
            "ggt_select(115)":"0",
            "ggt_select(116)":"2",
            "ggt_select(117)":"1",
            "ggt_textbox(119)":"",
            "ggt_textbox(121)":"",
            "ggt_textbox(122)":"",
            "ggt_select(145)":"0",
            "ggt_textbox(146)":"",
            "ggt_textbox(147)":"",
            "ggt_textbox(148)":"",
            "ggt_select(149)":"0",
            "ggt_select(150)":"2",
            "ggt_select(151)":"1",
            "ggt_textbox(152)":"",
            "ggt_textbox(153)":"",
            "ggt_select(177)":"0",
            "ggt_textbox(178)":"",
            "ggt_textbox(179)":"",
            "ggt_textbox(180)":"",
            "ggt_select(184)":"0",
            "ggt_select(185)":"2",
            "ggt_select(186)":"1",
            "ggt_hidden(193)":"",
            "ggt_hidden(194)":"",
            "ggt_hidden(251)":"0 }", }
        self.setName(name)
        self.setEmail(email)

    def setName(self, name):
        self.address_entry_data[NAME_FIELD] = name

    def setEmail(self, email):
        self.address_entry_data[EMAIL_FIELD] = email
