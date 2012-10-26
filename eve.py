import groupbotlib
import sys

if sys.argv[1]:
    eve = groupbotlib.groupbot("Eve")
    eve.connectGmail("eve.goupbot@gmail.com","17324430645.17019220200.fn7rGcMgCG@txt.voice.google.com","eve.goupbot","nanat103")
    eve.setMessage(sys.argv[1])
    eve.sendMessage()
    eve.disconnectGmail()
