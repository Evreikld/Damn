
import io
from sys import api_version
from unittest import result
from xmlrpc.client import Boolean

i=1
score=u''


Test=u'"test":"d",'
filescore="Name.txt"
 
Test=u'test'


#World

Macron=u'Macron'
Albert=u'"Albert II"'
Duda=u'"Duda"'
Mattarella=u'"Mattarella"'
Steinmeier=u'"Steinmeier"'
Bolsonaro='"Bolsonaro"'
Obrador=u'Obrador'
Bukele=u'"Bukele"'
Fernandez=u'"Fernandez"'
Kovind='"Kovind"'
Trudeau=u'"Trudeau"'
Jinping=u'"Jinping"'
Lee=u'"Lee Kuan Yew"'
Moon='"Moon Jae In"'

#Special

Satochi=u'"Satoshi"'
Secret='"Secret"'

#USA

Biden=u'Biden'
Obama=u'Obama'
Trump=u'Trump'
Clinton=u'Clinton'

#World Legends

deGaulle=u'de Gaulle'
Churchill=u'Churchill'
CheGuevara=u'Che Guevara'
Castro=u'Castro'

#USA Legends

Franklin=u'Франклин-1'
Carter=u'Carter'
Nixon=u'Kennedy'
Kennedy=u'Kennedy'
Lincoln=u'Lincoln'
Roosevelt=u'"Theodore Roosevelt"'
Reagan=u'Reagan'
Bush=u'Bush'
Washington=u'Washington'
Jefferson=u'Jefferson'
Madison=u'Madison'

#Crypto

Buterin=u'Buterin'
Sun=u'"Sun"'
Zhao=u'Zhao'
Bankman=u'Bankman-Fried'
Jihan=u'Jihan'
Hoskinson=u'Hoskinson'
Armstrong=u'Armstrong'
Ver=u'"Ver"'
LeeCrypt=u'"Lee"'
Cameroon=u'"Cameron Winklevoss"'
TylerWinklevoss=u'Tyler Winklevoss'
McCaleb=u'McCaleb'
Larens=u'Larens'

Macron=u'E.M.'
Albert=u'A.II'
#Soviet

Stalin=u'Stalin'
Brezhnev=u'Brezhnev'
Gorbachev=u'Gorbachev'


#Check

End_file=u']'


while i<20002:
    filename="%d.json" % i 
    i+=1 
    score=u''
    with io.open(filename, encoding='utf-8') as file:
        for line in file:
            
            #World
            
            if Macron in line:
              Macron=u'E.M.'  
            if Albert in line:
              Albert=u'A.II'
            if Duda in line:
              Duda=u'A.D.'  
            if Mattarella in line:
              Mattarella=u'S.M.'
            if Steinmeier in line:
              Steinmeier=u'F.-W.S.'  
            if Bolsonaro in line:
              Bolsonaro=u'J.M.B.'
            if Obrador in line:
              Obrador=u'A.M.'  
            if Bukele in line:
              Bukele=u'N.B.'
            if Fernandez in line:
              Fernandez=u'A.F.'  
            if Kovind in line:
              Kovind=u'R.N.K.'
            if Trudeau in line:
              Trudeau=u'J.T.'  
            if Jinping in line:
              Jinping=u'X.J.'
            if Lee in line:
              Lee=u'L.K.Y.'  
            if Moon in line:
              Moon=u'M.J.I.'
            
            #Usa
            
            if Biden in line:
              Biden=u'J.B.'  
            if Obama in line:
              Obama=u'B.O.'
            if Trump in line:
              Trump=u'D.T.'  
            if Clinton in line:
              Clinton=u'B.C.'
            
            #World Legends
            
            if Churchill in line:
              Churchill=u'W.C.'  
            if deGaulle in line:
              deGaulle=u'C.G.'
            if CheGuevara in line:
              CheGuevara=u'E.C.G.'  
            if Castro in line:
              Castro=u'F.C.'
              
            #Usa Legends
            
            if Franklin in line:
              Franklin=u'F.R.'  
            if Carter in line:
              Carter=u'J.C.'
            if Nixon in line:
              Nixon=u'R.N.'  
            if Kennedy in line:
              Kennedy=u'J.K.'
            if Lincoln in line:
              Lincoln=u'A.L.'  
            if Roosevelt in line:
              Roosevelt=u'T.R.'
            if Reagan in line:
              Reagan=u'R.R.'  
            if Bush in line:
              Bush=u'G.B.'
            if Washington in line:
              Washington=u'G.W.'  
            if Jefferson in line:
              Jefferson=u'T.J.'
            if Madison in line:
              Madison=u'J.M.'  
            
            #Soviet
            
            if Stalin in line:
              Stalin=u'J.V.S.'  
            if Brezhnev in line:
              Brezhnev=u'L.B.'
            if Gorbachev in line:
              Gorbachev=u'M.G.'  
              
             #Crypto
            
            if Buterin in line:
              Buterin=u'V.B.'  
            if Sun in line:
              Sun=u'J.S.'
            if Zhao in line:
              Zhao=u'C.Z.'  
            if Bankman in line:
              Bankman=u'S.B.-F.'
            if Jihan in line:
              Jihan=u'J.W.'  
            if Hoskinson in line:
              Hoskinson=u'C.H.'
            if Armstrong in line:
              Armstrong=u'B.A.'  
            if Ver in line:
              Ver=u'R.V.'
            if LeeCrypt in line:
              LeeCrypt=u'Ch.L.'  
            if Cameroon in line:
              Cameroon=u'C.W.'
            if TylerWinklevoss in line:
              TylerWinklevoss=u'T.W.'
            if McCaleb in line:
              McCaleb=u'J.M.'
            if Larens in line:
              Larens=u'C.L.'  
            
              
           #Special
           
            if Satochi in line:
              Satochi=u'S.N.'  
            if Secret in line:
              Secret=u'Secret'                      
                   
            if End_file in line:       
                with open (filescore,'a') as f:
                    f.write(f"{filename} {score}\n")
                    print(i,'printed')
                    
                    
 
                                 
                   
                   
                   
                
