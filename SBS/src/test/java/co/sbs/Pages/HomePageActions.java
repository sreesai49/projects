package co.sbs.Pages;

import co.sbs.config.ContextManager;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.FindBys;
import org.openqa.selenium.support.PageFactory;
import org.testng.Assert;

import java.util.List;
import java.util.Locale;

public class HomePageActions {

    CommonActions commonActions() {return new CommonActions();}

    @FindBy(xpath = "//h1")
    private WebElement title;

    @FindBy(xpath = "//a[contains(text(), 'DOWNLOAD')]")
    private WebElement downloadElement;

    @FindBy(xpath = "//div[contains(@class, 'podcast-subscribe__label')]")
    private WebElement subscribeElement;

    @FindBy(xpath = "//*[contains(@class, 'audiotrack__image')]//button")
    private WebElement playButton;

    @FindBys({@FindBy(xpath = "//*[@class='podcast-subscribe__list']//a")})
    private List<WebElement> subscribeOptions;

    @FindBy(id = "mod-audio-player_module-1")
    private WebElement audioPlayer;

    @FindBy(xpath = "//*[@id='mod-audio-player_module-1']//img")
    private WebElement playerPanelImage;

    @FindBy(xpath = "//*[@class='audio-player__info-panel-content']")
    private WebElement audioPlayerContent;

    @FindBy(xpath = "//*[@aria-label='Playback speed']")
    private WebElement playBackSpeed;

    @FindBy(xpath = "//*[@aria-label='Previous Track']")
    private WebElement previousTrackButton;

    @FindBy(xpath = "//*[@aria-label='Step back 20 seconds']")
    private WebElement stepBackButton;

    @FindBy(xpath = "//*[@class='audio-player__controls']//*[@aria-label='Play']")
    private WebElement playPauseButton;

    @FindBy(xpath = "//*[@aria-label='Step forward 20 seconds']")
    private WebElement stepForwardButton;

    @FindBy(xpath = "//*[@aria-label='Next Track']")
    private WebElement nextTrackButton;

    @FindBy(xpath = "//*[@aria-label='Mute']")
    private WebElement muteButton;

    @FindBy(xpath = "//*[@aria-label='Elapsed Time']")
    private WebElement elapsedTime;

    @FindBy(xpath = "//*[@aria-label='Duration']")
    private WebElement totalTime;

    @FindBy(xpath = "//*[@class='audio-player__volume-level']")
    private WebElement volumeLevel;

    @FindBy(xpath = "//*[@class='audio-player__progress']")
    private WebElement audioPlayerProgress;

    @FindBy(xpath = "//*[@data-type='toggle-language']")
    private WebElement languageToggle;

    @FindBy(xpath = "//pre")
    private WebElement jsonContent;

    @FindBy(xpath = "//video")
    private WebElement planeAudioPlayer;

    public WebElement getTitle() {
        return title;
    }

    public WebElement getSubscribeElement() {
        return subscribeElement;
    }

    public WebElement getDownloadElement() {
        return downloadElement;
    }

    public WebElement getPlayButton() {
        return playButton;
    }

    public void verifySubscribeOptions() {
        Assert.assertTrue(commonActions().isElementPresent(subscribeOptions.get(0)));
        Assert.assertEquals(subscribeOptions.get(0).getText(), "APPLE PODCASTS");
        Assert.assertTrue(commonActions().isElementPresent(subscribeOptions.get(1)));
        Assert.assertEquals(subscribeOptions.get(1).getText(), "GOOGLE PODCASTS");
        Assert.assertTrue(commonActions().isElementPresent(subscribeOptions.get(2)));
        Assert.assertEquals(subscribeOptions.get(2).getText(), "SPOTIFY");
    }

    public WebElement getAudioPlayer() {
        return audioPlayer;
    }

    public void verifyAudioPlayerElements() {
        commonActions().isElementAssertTrue(playerPanelImage, "Panel image is not appearing");
        commonActions().isElementAssertTrue(audioPlayerContent, "Audio player content is not appearing");
        Assert.assertEquals(audioPlayerContent.getText().split("\n")[1], getTitle().getText());
        commonActions().isElementAssertTrue(playBackSpeed, "Play back speed is not appearing");
        commonActions().isElementAssertTrue(previousTrackButton, "Previous track button is not appearing");
        commonActions().isElementAssertTrue(stepBackButton, "Step back button is not appearing");
        commonActions().isElementAssertTrue(playPauseButton, "Play pause button is not appearing");
        commonActions().isElementAssertTrue(stepForwardButton, "Step forward button is not appearing");
        commonActions().isElementAssertTrue(nextTrackButton, "Next track button is not appearing");
        commonActions().isElementAssertTrue(muteButton, "Mute button is not appearing");
        commonActions().isElementAssertTrue(elapsedTime, "Elapsed time is not appearing");
        commonActions().isElementAssertTrue(totalTime, "Total time is not appearing");
    }

    public WebElement getPlayPauseButton() {
        return playPauseButton;
    }

    public WebElement getElapsedTime() {
        return elapsedTime;
    }

    public String getAudioVolumeLevel() {
        return volumeLevel.getAttribute("style").split(":")[1].trim();
    }

    public WebElement getMuteButton() {
        return muteButton;
    }
    public WebElement getStepForwardButton() {return stepForwardButton;}

    public WebElement getStepBackButton() {return stepBackButton;}

    public WebElement getAudioPlayerProgress() {return audioPlayerProgress;}

    public WebElement getLanguageToggle() {return languageToggle;}

    public WebElement getJsonContent() {return jsonContent;}

    public WebElement getSimpleAudioPlayer() {return planeAudioPlayer;}
}
