; ModuleID = '../src/test68.c'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: nounwind
define i32 @test68(i32 %var1, i32 %var2, i32 %var3, i32 %var4, i32 %var5) #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  %5 = alloca i32, align 4
  store i32 %var1, i32* %1, align 4
  store i32 %var2, i32* %2, align 4
  store i32 %var3, i32* %3, align 4
  store i32 %var4, i32* %4, align 4
  store i32 %var5, i32* %5, align 4
  %6 = load i32, i32* %1, align 4
  %7 = load i32, i32* %2, align 4
  %8 = icmp sge i32 %6, %7
  br i1 %8, label %9, label %22

; <label>:9                                       ; preds = %0
  %10 = load i32, i32* %1, align 4
  %11 = load i32, i32* %2, align 4
  %12 = icmp eq i32 %10, %11
  br i1 %12, label %13, label %17

; <label>:13                                      ; preds = %9
  %14 = load i32, i32* %3, align 4
  %15 = load i32, i32* %4, align 4
  %16 = add nsw i32 %14, %15
  store i32 %16, i32* %3, align 4
  br label %21

; <label>:17                                      ; preds = %9
  %18 = load i32, i32* %3, align 4
  %19 = load i32, i32* %5, align 4
  %20 = add nsw i32 %18, %19
  store i32 %20, i32* %3, align 4
  br label %21

; <label>:21                                      ; preds = %17, %13
  br label %22

; <label>:22                                      ; preds = %21, %0
  %23 = load i32, i32* %3, align 4
  ret i32 %23
}

attributes #0 = { nounwind "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "stack-protector-buffer-size"="8" "target-features"="+mmx,+sse,+sse2" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.ident = !{!0}

!0 = !{!"clang version 3.8.0-2ubuntu4 (tags/RELEASE_380/final)"}
