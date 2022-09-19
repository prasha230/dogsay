import sys
def dog_say(msg):
    msg=' '.join(msg)

    max_chars_in_one_line=30

    if(len(msg)>max_chars_in_one_line):
        para=[]
        for i in range(0,len(msg),max_chars_in_one_line):               #breaking whole message into line of 'max_chars_in_one_line' size
            para.append(msg[i:i+max_chars_in_one_line].ljust(max_chars_in_one_line))
        
        print('','_'*(max_chars_in_one_line+2))         #top border
        for i in range(len(para)):
            print('|',para[i],'|')
        print('','_'*(max_chars_in_one_line+2))         #bottom border
    else:
        print('','_'*(len(msg)+2))
        print('|',msg,'|')
        print('','-'*(len(msg)+2))
    print('     \|')
    print('      \ ')
    print('        , ')
    print('        |`-.__')
    print("        /   _/")
    print('       ****`')
    print('      /    }')
    print('     /  \ /')
    print(' \ /`   \\\ ')
    print('  `\    /_\\')
    print('   `~~~~~``~`')
dog_say(sys.argv[1:])