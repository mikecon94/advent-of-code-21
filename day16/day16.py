f = open("input", "r")

hexToBin = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111'
    }

binaryInput = ""
for char in f.readline().strip():
    binaryInput += hexToBin[char]

# First 3 Bits
def getVersion(binary):
    return int(binary[0:3], 2)

# Second 3 Bits
def getTypeId(binary):
    return int(binary[3:6], 2)

# Used when Type ID = 4
def parseLiteralValue(binary):
    # Parses from after the Type ID Bit
    binaryValue = ""
    end = False
    for bit in range(6, len(binary), 5):
        if (end): break
        if (binary[bit] == '0'):
            end = True
        binaryValue += binary[bit+1:bit+5]
        parsedTo = bit+5
    return int(binaryValue, 2), parsedTo

# Used when Type ID != 4
def parseOperator(binary):
    # Parses from after the Type ID Bit
    lengthTypeId = int(binary[6], 2)
    # If Length Type ID = 0
    # The next 15 bits are total length of sub-packets contained by this packet
    if(lengthTypeId == 0):
        # Tells us the length of the next subpackets
        subPacketsLength = int(binary[7:22], 2)
        print("Op Sub Packet Length:", subPacketsLength)
        # Need to know when a sub-packet ends to be able to parse the next one.
        parsedTo = 22
        while(parsedTo < (subPacketsLength + 22) ):
            result = parsePacket(binary[parsedTo:])
            output = result[0]
            parsedTo += result[1]

        parsedTo = 22 + subPacketsLength
    # If Length Type ID = 1
    # The next 11 bits are a number that represents the number of sub-packets contained.
    elif(lengthTypeId == 1):
        noOfSubPackets = int(binary[7:18], 2)
        parsedTo = 18
        print("Op No Of Sub Packets:", noOfSubPackets)
        # Need to know when a sub-packet ends to be able to parse the next one.
        packetsParsed = 0
        while (packetsParsed < noOfSubPackets):
            result = parsePacket(binary[parsedTo:])
            output = result[0]
            parsedTo += result[1]
            packetsParsed += 1

    # Perform the operation on the outputs of the sub-packets

    # Return operator Output & Bit parsed until
    return 0, parsedTo

sumOfVersions = 0
def parsePacket(packet):
    print(packet)
    print("Version:", getVersion(packet))
    global sumOfVersions
    sumOfVersions += getVersion(packet)
    typeId = getTypeId(packet)
    if(typeId == 4):
        result = parseLiteralValue(packet)
        outputValue = result[0]
        parsedTo = result[1]
        print("Literal:", outputValue)
    else:
        print("Operator")
        result = parseOperator(packet)
        outputValue = result[0]
        parsedTo = result[1]

    # Return Bit Index Packet was parsed to
    return outputValue, parsedTo

parsePacket(binaryInput)

print("Total Versions:",sumOfVersions)