package co.sbs.config;

import org.openqa.selenium.WebDriver;

public class ContextManager {

//    private static ThreadLocal<WebDriver> webDriver = new ThreadLocal<>();
    private static WebDriver webDriver;

    public static WebDriver getDriver() {
        return webDriver;
    }

    public static void setDriver(WebDriver driver) {
        webDriver = driver;
    }

}
