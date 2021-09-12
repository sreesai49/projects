package co.sbs.Pages;

import co.sbs.config.ContextManager;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.google.gson.JsonArray;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import org.openqa.selenium.*;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.FluentWait;
import org.openqa.selenium.support.ui.Wait;
import org.testng.Assert;

import java.time.Duration;
import java.util.ArrayList;
import java.util.List;

public class CommonActions {
    public static WebDriver driver;

    public CommonActions() {
        driver = ContextManager.getDriver();
    }

    public void waitInSec(int sec) {
        try {
            Thread.sleep(sec*1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    public void waitTillElement(WebElement element) {
        Wait fluentWait = new FluentWait(driver).withTimeout(Duration.ofSeconds(30)).ignoring(StaleElementReferenceException.class,
                NoSuchElementException.class).pollingEvery(Duration.ofSeconds(2));
        fluentWait.until(ExpectedConditions.refreshed(ExpectedConditions.visibilityOf(element)));
    }

    public boolean isElementPresent(WebElement element) {
        boolean flag = false;
        try {
            waitTillElement(element);
            for (int i = 0; i < 10; i++) {
                if (element.isDisplayed()) {
                    flag = true;
                    break;
                } else {
                    waitInSec(1);
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return flag;
    }

    public void isElementAssertTrue(WebElement element, String message) {
        Assert.assertTrue(isElementPresent(element), message);
    }

    public void scrollToElement(WebElement element) {
        JavascriptExecutor js = (JavascriptExecutor) driver;
        for (int i = 0; i < 5; i++) {
            if (isElementPresent(element)) {
                break;
            } else {
                js.executeScript("window.scrollBy(0,250)", "");
            }
        }
    }

    public String addTime(String baseTime, int time) {
        int hr = Integer.parseInt(baseTime.split(":")[0]);
        int sec = Integer.parseInt(baseTime.split(":")[1]);
        if ((sec+time) > 60) {
            sec = time-60;
            hr = hr+1;
        } else {
            sec = sec+time;
        }
        return String.valueOf(hr)+":"+String.valueOf(sec);
    }

    public String differenceTime(String baseTime, int time) {
        int hr = Integer.parseInt(baseTime.split(":")[0]);
        int sec = Integer.parseInt(baseTime.split(":")[1]);
        if ((sec-time) < 0) {
            sec = 60-(time-sec);
            hr = hr-1;
        } else {
            sec = sec-time;
        }
        return String.valueOf(hr)+":0"+String.valueOf(sec);
    }

    public void hoverOnElement(WebElement element) {
        Actions actions = new Actions(driver);
        actions.moveToElement(element);
    }

    public List<String> getAudioFilesFromJson(String jsonContent) throws JsonProcessingException {
        ObjectMapper mapper = new ObjectMapper();
        JsonNode node = mapper.readTree(jsonContent);
        List<String> audioUrls = new ArrayList<String>();
        for (int i = 0; i < node.size(); i++) {
            audioUrls.add(node.get(i).get("archiveAudio").get("mp3").asText());
        }
        return audioUrls;
    }

}
