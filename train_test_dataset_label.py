class train_test_dataset_label:

    def get_train_positive(self):
        train_positive_tweets = open("PositiveTrain.txt", 'r').read().split('\n')

        return train_positive_tweets

    def get_train_negative(self):
        train_negative_tweets = open("NegativeTrain.txt", 'r').read().split('\n')

        return train_negative_tweets

    def get_train_neutral(self):
        train_neutral_tweets = open("NeutralTrain.txt", 'r').read().split('\n')

        return train_neutral_tweets

    def get_test_positive(self):
        test_positive_tweets = open("PositiveTest.txt", 'r').read().split('\n')

        return test_positive_tweets

    def get_test_negative(self):
        test_negative_tweets = open("NegativeTest.txt", 'r').read().split('\n')

        return test_negative_tweets

    def get_test_neutral(self):
        test_neutral_tweets = open("PositiveTest.txt", 'r').read().split('\n')

        return test_neutral_tweets


    def get_training_dataset(self):

        training_dataset = []

        for tweets in self.get_train_positive(self):

            training_dataset.append((tweets, '1'))

        for tweets in self.get_train_negative(self):

            training_dataset.append((tweets, '-1'))

        for tweets in self.get_train_neutral(self):

            training_dataset.append((tweets, '0'))

        return training_dataset


    def get_testing_dataset(self):

        testing_dataset = []

        for tweets in self.get_test_positive(self):

            testing_dataset.append((tweets))

        for tweets in self.get_test_negative(self):

            testing_dataset.append((tweets))

        for tweets in self.get_test_neutral(self):

            testing_dataset.append((tweets))

        return testing_dataset
