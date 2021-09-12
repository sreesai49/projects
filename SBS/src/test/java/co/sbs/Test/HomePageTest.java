package co.sbs.Test;

import co.sbs.Pages.CommonActions;
import co.sbs.Pages.HomePageActions;
import co.sbs.config.ContextManager;
import com.fasterxml.jackson.core.JsonProcessingException;
import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.PageFactory;
import org.testng.Assert;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.List;
import java.util.Properties;

public class HomePageTest {

    private Properties prop = new Properties();
    HomePageActions homePageActions = new HomePageActions();
    CommonActions commonActions() {return new CommonActions();}
    public WebDriver driver;

    HomePageTest() {
        String configFile = System.getProperty("user.dir")+ "/src/test/java/co/sbs/config/" + "config.properties";
        try (FileInputStream inputStream = new FileInputStream(configFile)) {
            prop.load(inputStream);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @BeforeClass
    public void beforeClass() {
        WebDriverManager.chromedriver().setup();
        driver = new ChromeDriver();
        ContextManager.setDriver(driver);
        driver.manage().window().maximize();
        driver.get(prop.getProperty("url"));
        PageFactory.initElements(driver, homePageActions);
    }

    @AfterClass
    public void afterClass() {
        driver.quit();
    }

    @Test(alwaysRun = true)
    public void testHindiRadio() {
        //verify the title of the audio track
        boolean isTitle = commonActions().isElementPresent(homePageActions.getTitle());
        Assert.assertTrue(isTitle, "Title is not appearing");
        boolean isDownload = commonActions().isElementPresent(homePageActions.getDownloadElement());
        Assert.assertTrue(isDownload, "Download is not appearing");
        boolean isSubscribe = commonActions().isElementPresent(homePageActions.getSubscribeElement());
        Assert.assertTrue(isSubscribe, "Subscribe is not appearing");
        //Verify Subscribe dropdown displays apple and google podcasts
        homePageActions.getSubscribeElement().click();
        homePageActions.verifySubscribeOptions();
        homePageActions.getSubscribeElement().click();
        //Click Play on the audio icon and verify audio player is launched at the bottom of the screen
        commonActions().scrollToElement(homePageActions.getPlayButton());
        homePageActions.getPlayButton().click();
        commonActions().waitTillElement(homePageActions.getAudioPlayer());
        homePageActions.verifyAudioPlayerElements();
        //Click and verify player controls – Play and pause, mute and unmute
        homePageActions.getPlayPauseButton().click();
        String audioPlayedTime = homePageActions.getElapsedTime().getText();
        commonActions().waitInSec(4);
        Assert.assertEquals(audioPlayedTime, homePageActions.getElapsedTime().getText()); // To check audio is paused
        homePageActions.getPlayPauseButton().click();
        Assert.assertEquals(homePageActions.getAudioVolumeLevel(), "100%;");
        homePageActions.getMuteButton().click();
        Assert.assertEquals(homePageActions.getAudioVolumeLevel(), "0%;");
        homePageActions.getMuteButton().click();
        //Click 20s forward or rewind on the audio player and verify scrub on the progress bar
        homePageActions.getPlayPauseButton().click();
        String elapsedTime = homePageActions.getElapsedTime().getText();
        String beforeProgress = homePageActions.getAudioPlayerProgress().getAttribute("style").split(":")[1].trim();
        homePageActions.getStepForwardButton().click();
        Assert.assertEquals("0"+commonActions().addTime(elapsedTime, 20), homePageActions.getElapsedTime().getText());
        String afterProgress = homePageActions.getAudioPlayerProgress().getAttribute("style").split(":")[1].trim();
        Assert.assertNotEquals(beforeProgress, afterProgress);
        //Step backward
        elapsedTime = homePageActions.getElapsedTime().getText();
        beforeProgress = homePageActions.getAudioPlayerProgress().getAttribute("style").split(":")[1].trim();
        homePageActions.getStepBackButton().click();
        Assert.assertEquals("0"+commonActions().differenceTime(elapsedTime, 20), homePageActions.getElapsedTime().getText());
        afterProgress = homePageActions.getAudioPlayerProgress().getAttribute("style").split(":")[1].trim();
        Assert.assertNotEquals(beforeProgress, afterProgress);
        //Verify clicking on language toggle (top right corner of the page) displays language list
        commonActions().hoverOnElement(homePageActions.getLanguageToggle());
        homePageActions.getLanguageToggle().click();
    }

    @Test
    public void validateTheAPIResponseObject() throws JsonProcessingException {
        driver.get(prop.getProperty("apiUrl"));
        commonActions().waitTillElement(homePageActions.getJsonContent());
        String jsonString = homePageActions.getJsonContent().getText();
        List<String> audioUrls = commonActions().getAudioFilesFromJson(jsonString);
        for (String url : audioUrls) {
            driver.get(url);
            commonActions().isElementAssertTrue(homePageActions.getSimpleAudioPlayer(), "Audio player is not appearing");
        }
    }
}
