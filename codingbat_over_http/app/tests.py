from django.test import SimpleTestCase

# Create your tests here.
class TestFrontView(SimpleTestCase):
    def test_chocolate_2(self):
        response = self.client.get("/warmup-2/front-times/?input_text=chocolate&num_r=2")
        self.assertContains(response, "chocho")
    def test_chocolate_3(self):
        response = self.client.get("/warmup-2/front-times/?input_text=chocolate&num_r=3")
        self.assertContains(response, "chochocho")
    def test_abc_3(self):
        response = self.client.get("/warmup-2/front-times/?input_text=abc&num_r=3")
        self.assertContains(response, "abcabcabc")

class TestTeenView(SimpleTestCase):
    def test_1_2_3(self):
        response = self.client.get("/logic-2/no-teen-sum/?n1=1&n2=2&n3=3")
        self.assertContains(response, "6")
    def test_2_13_1(self):
        response = self.client.get("/logic-2/no-teen-sum/?n1=2&n2=13&n3=1")
        self.assertContains(response, "3")
    def test_2_1_14(self):
        response = self.client.get("/logic-2/no-teen-sum/?n1=2&n2=1&n3=14")
        self.assertContains(response, "3")
    
class TestXYZView(SimpleTestCase):
    def test_abcxyz_true(self):
        response = self.client.get("/string-2/xyz-there/?str=abcxyz")
        self.assertContains(response, "True")
    def test_abc_xyz_false(self):
        response = self.client.get("/string-2/xyz-there/?str=abc.xyz")
        self.assertContains(response, "False")
    def test_xyz_abc_true(self):
        response = self.client.get("/string-2/xyz-there/?str=xyz.abc")
        self.assertContains(response, "True")


class TestAvgView(SimpleTestCase):
    def test_1234100(self):
        response = self.client.get("/list-2/centered-average/?n1=1&n2=2&n3=3&n4=4&n5=100")
        self.assertContains(response, "3")
    def test_11551087(self):
        response = self.client.get("/list-2/centered-average/?n1=11&n2=55&n3=1&n4=0&n5=87")
        self.assertContains(response, "22.333333333333332")
    def test_1042420(self):
        response = self.client.get("/list-2/centered-average/?n1=-10&n2=-4&n3=-2&n4=-4&n5=-2")
        self.assertContains(response, "-3")