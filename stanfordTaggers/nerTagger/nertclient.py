import re
import socket

de_newline = re.compile('\n')
def nertclient(document, port = 9000):
    document = re.sub(de_newline, " ", document) + "\n"

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost", port))

    # send
    payload = document.encode()
    bytes_to_send = len(payload)
    bytes_sent = 0
    while bytes_sent < bytes_to_send:
        sent = s.send(payload[bytes_sent:])
        bytes_sent += sent

    # receive. server delimits by 0x20 0x0a
    result = b""
    while not(len(result) >= 2 and result[-2] == 0x20 and result[-1] == 0x0a):
        result += s.recv(1024)
    result = result.decode()
    result = re.sub(de_newline, " ", result)

    return result

if __name__ == "__main__":
    test1 = "Wenqin is a \nstudent at UC Berkeley in California\n"
    test2 = '''The cartoon begins with the camera panning across several items on a
    table, including a book entitled "How to Hunt Ducks" and freshly opened
    boxes which recently contained a shotgun, hunting suit, duck decoys and
    shells. The camera then pans to Porky in front of a mirror, admiring
    himself in various poses with his new rifle and hunting suit. Porky points
    his shotgun at various imaginary aerial targets, then points it at his dog
    Rover; the dog runs under and into a bureau. Porky tells him the gun is not
    loaded and pulls the trigger to prove it. However, the shotgun actually is
    loaded and it fires into the ceiling. The man upstairs, shot in one butt
    cheek, comes down to punch Porky in the nose. The scene changes to a lake,
    pre-dawn. Porky spies a duck, but before he can get off a shot, lots of
    other previously hidden duck hunters suddenly appear and shoot at it for
    several seconds. They all miss. The duck hunters say "Aw, shucks!" in
    unison when they fail to shoot the duck. A cross-eyed duck hunter tries to
    shoot the same duck  but instead shoots down two airplanes. Porky puts out
    duck decoys. Daffy appears among them and acts like a fake duck. Porky
    tries to shoot Daffy after donning a decoy on his head and sneaking
    underwater, but the gun shoots out water instead of bullets. Daffy then
    flies onto a floating barrel . Porky shoots the whiskey-filled barrel but
    Daffy escapes. Some fish are attracted to the leaking barrel and get drunk.
    The fish come onshore, commandeer a boat and drunkenly sing 'On Moonlight
    Bay'. Porky Pig observes that something is 'fishy' with those fish. Porky
    then hears a quack nearby. When he looks into the grass, Daffy bites his
    nose. Daffy then takes to the sky; Porky shoots him with a single shot.
    Ecstatic, Porky instructs his dog Rover  and the dog swims out, but when he
    comes back, it's Daffy carrying the dog and throwing him back on the bank.
    Porky whips out a notepad, leafs through it and notes that this scene
    'wasn't in the script'  . Daffy yells out his first words, that he is "just
    a crazy, darn fool duck", and proceeds to do his signature 'crazy dance' on
    the lake. After a humorous scene where Daffy eats an electric eel and turns
    into a lightning bolt, Porky tries hunting from a rowboat but is taunted by
    the ducks when he stops for lunch; in his hurry to fire at them he
    inadvertently sinks the boat, cueing Joe Penner to rise from underneath the
    water with his signature line "You wanna buy a duck?" After being alerted
    by his dog that Daffy is back, Porky makes several attempts to cock the gun
    and shoot, but the gun fails to fire each time. Daffy comes out of the
    water, takes the gun and fires it after the first cock. After saying "It's
    me again," Daffy does another crazy dance. Daffy takes to the air and is
    met by Porky shooting his gun rapid-fire and being driven into the ground
    by the recoil, apparently not hitting anything. Porky tries to use a duck
    call, but the other duck hunters mistake it for a real duck and shoot at
    Porky, who ducks for cover. Disgusted, Porky throws the duck call to the
    ground, but it bounces and his dog accidentally swallows it. The dog gets
    the hiccups, quacking with every one, drawing constant fire and forcing
    Porky and the dog to flee from the lake. Porky and the dog trudge home,
    disappointed with their failure to bag a duck. When Porky gets home, he
    sees the ducks outside doing a trapeze act in the sky at his window. Porky
    tries to shoot them with his gun but, thinking the gun empty, throws the
    shotgun to the floor. The gun fires into the ceiling. The cartoon ends with
    the man from upstairs, with his other butt cheek shot, coming down once
    again to punch Porky in the nose. The cartoon ends with Daffy jumping
    around the standard "That's all, Folks!" closing title, accompanied by "The
    Farmer In The Dell."'''
    print(nertclient(test1))
    print(nertclient(test2))
