import notify2
import rates


def notify():

    nbu = rates.fetch_nbu_currency()
    notify2.init("NBU currency rates")

    n = notify2.Notification("Currency Notifier", message=str(nbu))
    n.set_urgency(notify2.URGENCY_NORMAL)
    n.set_timeout(10000)

    n.show()


notify()
