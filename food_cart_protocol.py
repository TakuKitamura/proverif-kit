import random


class FoodStandProtocol():
    def __init__(self, canFakeFoodStandName, canFaketicketID):

        self.ticketsInfo = {
            '焼きそば屋': [5, 6, 7, 8, 9],
            'たこ焼き屋': [9, 10, 20],
            'たません屋': [100, 105, 110],
            'わた菓子屋': [20, 21, 100]
        }

        foodStandsName = list(self.ticketsInfo.keys())

        print('| ', end='')
        for i, v in enumerate(foodStandsName):
            print("{}. {}".format(i + 1, v), end=' | ')
        print()

        self.foodStandSelectedByCustomer = foodStandsName[int(
            input('食券を買う店の番号(num): ')) - 1]

        self.customerTicket = {
            'foodStandName': self.foodStandSelectedByCustomer,
            'ticketID': random.choice(self.ticketsInfo[self.foodStandSelectedByCustomer])
        }

        print('「{}」の食券番号「{}」番の食券を受け取りました'.format(
            self.customerTicket['foodStandName'], self.customerTicket['ticketID']))

        if canFakeFoodStandName:
            self.customerTicket['foodStandName'] = input(
                '店舗名を何に偽造しますか？(str): ')

        if canFaketicketID:
            self.customerTicket['ticketID'] = int(
                input('食券番号を何番に偽造しますか?(num): '))

        print()

    def ticketMachineGiveTicketToCustomer(self):
        print('食券機がお客に食券を発券します')
        return self.customerTicket

    def customerHandTicketToSeller(self, ticket):
        print('お客が屋台の人に食券を渡します')
        return self.sellerCheckTicket(ticket)

    def sellerCheckTicket(self, ticket):
        print('屋台の人が食券の確認を行います')
        if (ticket['foodStandName'] == self.foodStandSelectedByCustomer):
            print('屋台の人は食券は私の店のものであると確認しました')
            print('屋台の人がパソコンで食券番号の確認を行います')
            return self.pcTellResultOfAuthToSeller(ticket['ticketID'])
        else:
            print('屋台の人はお客に食券は私の店のものではないと伝えます')
            return [False, 'これは私の店の食券ではありません']

    def pcTellResultOfAuthToSeller(self, ticketID):
        print('パソコンは屋台の人に食券番号が正しいかどうか伝えます')
        ticketIDExist = ticketID in self.ticketsInfo[self.foodStandSelectedByCustomer]
        return self.sellerReplayToCustomer(ticketIDExist)

    def sellerReplayToCustomer(self, ticketIDExist):
        print('屋台の人はパソコンで食券番号が正しいどうか知りました')
        if ticketIDExist:
            print('屋台の人はパソコンで食券番号が正しいどうか知りました')
            print('屋台の人はお客さんに食券番号が正しいことを伝えます')
            return [True, '']
        else:
            print('屋台の人はパソコンで食券番号が正しくないと知りました')
            print('屋台の人はお客さんに食券番号が誤っていたことを伝えます')
            return [False, '食券番号が間違っています']


if __name__ == '__main__':
    fcp = FoodStandProtocol(canFakeFoodStandName=True, canFaketicketID=False)

    ticket = fcp.ticketMachineGiveTicketToCustomer()
    validTicket, errMsg = fcp.customerHandTicketToSeller(ticket)

    print()

    if validTicket:
        print('結果: 食べ物がもらえました')
    else:
        print('結果: 食べ物がもらえませんでした')
        print('理由: {}'.format(errMsg))
