class Agent:
    def __init__(self, name, stocks=10, backlogs=0, incoming_orders=0, incoming_deliveries=0):
        self.name = name
        self.stocks = stocks
        self.backlogs = backlogs
        self.incoming_orders = incoming_orders
        self.incoming_deliveries = incoming_deliveries
        self.cumulative_stock_cost = 0
        self.cumulative_backlog_cost = 0
        self.orders = list()

    def get_state(self):
        return {
            "name": self.name,
            "stock": self.stocks,
            "backlog": self.backlogs,
            "incoming orders": self.incoming_orders,
            "incoming_deliveries": self.incoming_deliveries,
            "cumulative_stock_cost ": self.cumulative_stock_cost,
            "cumulative_backlog_cost": self.cumulative_backlog_cost,
            "last_order": 0 if len(self.orders) == 0 else self.orders[-1]}

    def reset(self):
        self.stocks = 10
        self.backlogs = 0
        self.incoming_orders = 0
        self.incoming_deliveries = 0
        self.cumulative_stock_cost = 0
        self.cumulative_backlog_cost = 0
        self.orders = list()

    def to_string(self):
        return str(self.get_state())
